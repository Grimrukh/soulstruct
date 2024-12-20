from __future__ import annotations

__all__ = [
    "COMPARISON_NODES",
    "NEG_COMPARISON_NODES",

    "MAP_ID_RE",
    "COMMON_FUNC_IMPORT_RE",
    "RESTART_TYPES",
    "EVENT_DOCSTRING_RE",
    "CONDITION_GROUP_RE",
    "EVS_TYPES",
    "PY_TYPES",
    "BUILTIN_NAMES",
    "IGNORE_IMPORT_RE",
    "GAME_MODULE_RE",
    "EVENT_ARG_TYPE_MSG",

    "EventStatementTyping",
    "ConditionNodeTyping",
    "SkipReturnTyping",

    "EventInfo",
    "parse_event_arguments",
    "import_module",
    "import_from",
    "import_from_common_func",
    "define_args",
    "as_event_statement_node",
    "as_condition_node",
    "as_skip_return_node",

    "no_skip_or_negate_or_return",
    "negate_only",
    "skip_and_negate_and_return",
]

import ast
import importlib
import importlib.util  # TODO: needed? IDE doesn't think so...
import logging
import re
import typing as tp
from functools import wraps
from pathlib import Path

from soulstruct.base.game_types.basic_types import GAME_TYPE
from soulstruct.utilities.files import import_arbitrary_module
from ..emevd.utils import get_write_offset

from .exceptions import *

_LOGGER = logging.getLogger("soulstruct")


COMPARISON_NODES = {ast.Eq: 0, ast.NotEq: 1, ast.Gt: 2, ast.Lt: 3, ast.GtE: 4, ast.LtE: 5}
NEG_COMPARISON_NODES = {ast.Eq: 1, ast.NotEq: 0, ast.Gt: 5, ast.Lt: 4, ast.GtE: 3, ast.LtE: 2}

MAP_ID_RE = re.compile(r"m(\d\d)_(\d\d)_")
COMMON_FUNC_IMPORT_RE = re.compile(
    r"\n\s*#\s*\[COMMON_FUNC\]\s*\n+"
    r"from\s+(?P<module>\.*[.\w]+)\s+import\s+(?P<names>"
    r"\((?:\s*\w+\s*,?)+\s*\)"  # multi-line
    r"|\w+(?:,\s*\w+)*)"  # one line
)
RESTART_TYPES = {"ContinueOnRest": 0, "RestartOnRest": 1, "EndOnRest": 2}  # avoiding circular import
EVENT_DOCSTRING_RE = re.compile(r"(\d+)(:\s*.*)?", re.DOTALL)
CONDITION_GROUP_RE = re.compile(r"(MAIN|(AND|OR)_(\d+))")
EVS_TYPES = ("B", "b", "H", "h", "I", "i", "f", "s")
PY_TYPES = {"uchar": "B", "char": "b", "ushort": "H", "short": "h", "uint": "I", "int": "i", "float": "f", "str": "s"}
BUILTIN_NAMES = {"Condition", "MAIN", "slot", "event_layers"}.union(RESTART_TYPES.keys())
IGNORE_IMPORT_RE = re.compile(r"^import typing.*")
GAME_MODULE_RE = re.compile(r"^soulstruct\.(\w+)\..*$")

EVENT_ARG_TYPE_MSG = f"""
    fmt character in: {repr(EVS_TYPES)}
         fmt type in: ({', '.join(PY_TYPES.keys())})
           game type: e.g. `Flag`, `Character`, `Object`
         game typing: e.g. `FlagTyping`, `CharacterTyping`, `ObjectTyping`
     game type | int: e.g. `Flag | int`, `Character | int`, `Object | int`
"""


EventStatementTyping = tp.Union[ast.Expr, ast.For, ast.If, ast.Assign, ast.Return]
ConditionNodeTyping = tp.Union[ast.UnaryOp, ast.BoolOp, ast.Compare, ast.Name, ast.Attribute, ast.Call]
SkipReturnTyping = tp.Union[ast.UnaryOp, ast.Name, ast.Attribute, ast.Compare, ast.Call]


class EventInfo(tp.NamedTuple):
    name: str
    id: int
    args: dict[str, tuple[int, int]]
    arg_types: str
    arg_classes: dict[str, GAME_TYPE]
    on_rest_behavior: int
    nodes: list[ast.stmt]
    description: str


def parse_event_arguments(
    event_node: ast.FunctionDef, namespace: dict[str, tp.Any],
) -> tuple[dict[str, tuple[int, int]], str, dict[str, GAME_TYPE]]:
    """Parse argument nodes of given event function node and return:
        - dictionary mapping argument names to `(write_offset, size)` tuples for creating `EventArgRepl` instances
        - event's argument format string, e.g. `"iIIBh"`
        - dictionary mapping argument names (where applicable) to `GameObjectInt` subclasses
    """
    arg_names = []  # type: list[str]
    arg_types = ""
    arg_classes = {}  # type: dict[str, GAME_TYPE]

    if event_node.args.defaults:
        raise EVSSyntaxError(event_node, "You cannot provide default values for event arguments.")
    if event_node.args.vararg or event_node.args.kwarg:
        raise EVSSyntaxError(event_node, "You cannot use `*args` or `**kwargs` in event functions.")
    if event_node.args.kwonlyargs:
        raise EVSSyntaxError(event_node, "You cannot have keyword-only arguments in event functions.")

    for arg_node in event_node.args.args:
        arg_name = arg_node.arg
        if arg_name == "_":
            continue  # recommended intellisense placeholder for the first `slot` arg
        if arg_name in {"slot", "event_layers"}:
            # Previously raised an error here, but now allowing them for IDE purposes (but they do nothing). An error
            # will still be raised if you try to use either of these names in the event function body.
            continue
        arg_names.append(arg_name)

        arg_type_node = arg_node.annotation

        if isinstance(arg_type_node, ast.BinOp):
            # `{GameObjectInt} | int` type hints are accepted (but no others).
            if not isinstance(arg_type_node.op, ast.BitOr):
                raise EVSSyntaxError(
                    event_node,
                    f"Invalid event argument type: {repr(arg_type_node)}. "
                    f"Valid type hints: {EVENT_ARG_TYPE_MSG}"
                )
            if not isinstance(arg_type_node.left, ast.Name):
                raise EVSSyntaxError(
                    event_node,
                    f"Invalid event argument type (left of |): {repr(arg_type_node.left)}. "
                    f"Valid type hints: {EVENT_ARG_TYPE_MSG}"
                )
            if not isinstance(arg_type_node.right, ast.Name):
                raise EVSSyntaxError(
                    event_node,
                    f"Invalid event argument type (right of |): {repr(arg_type_node.right)}. "
                    f"Valid type hints: {EVENT_ARG_TYPE_MSG}"
                )
            left_name = arg_type_node.left.id
            right_name = arg_type_node.right.id
            if left_name == "int":
                arg_type_node = arg_type_node.right  # process class name below
            elif right_name == "int":
                arg_type_node = arg_type_node.left  # process class name below
            else:
                raise EVSSyntaxError(
                    event_node,
                    f"Invalid event argument type. If '|' is used, one side must be `int` and the other must be "
                    f"a game type. Valid type hints: {EVENT_ARG_TYPE_MSG}"
                )

        if isinstance(arg_type_node, ast.Constant) and isinstance(arg_type_node.value, str):
            if arg_type_node.value not in EVS_TYPES:
                raise EVSSyntaxError(
                    event_node,
                    f"Invalid event argument type string {repr(arg_type_node.value)}. "
                    f"Valid type hints: {EVENT_ARG_TYPE_MSG}"
                )
            arg_type = arg_type_node.value

        elif isinstance(arg_type_node, ast.Name):
            try:
                arg_type = PY_TYPES[arg_type_node.id]
            except KeyError:
                class_name = arg_type_node.id
                class_name = class_name.removesuffix("Typing")  # not decompiled but could be used
                try:
                    arg_class = namespace[class_name]
                except KeyError:
                    raise EVSSyntaxError(
                        event_node,
                        f"{repr(class_name)} is not a valid game type for argument hinting.",
                    )
                try:
                    fmt = arg_class.get_event_arg_fmt()
                except AttributeError:
                    raise EVSSyntaxError(
                        event_node,
                        f"{repr(class_name)} is not a valid game type for argument hinting.",
                    )
                else:
                    arg_classes[arg_name] = arg_class
                    arg_type = fmt
        else:
            raise EVSSyntaxError(
                event_node,
                f"Every event argument needs a type. Valid type hints: {EVENT_ARG_TYPE_MSG}"
            )

        arg_types += arg_type

    arg_dict = {name: value for name, value in zip(arg_names, define_args(arg_types))}

    return arg_dict, arg_types, arg_classes


def import_module(node: ast.Import, ignore_names: list[str] = ()) -> dict[str, tp.Any]:
    module_dict = {}
    for alias in node.names:
        name = alias.name
        if name in ignore_names:
            continue
        try:
            module = importlib.import_module(alias.name)
            importlib.reload(module)
        except ImportError as e:
            raise EVSImportError(node, alias.name, str(e))
        as_name = alias.asname if alias.asname is not None else name
        try:
            module_dict[as_name] = getattr(module, name)
        except AttributeError as e:
            raise EVSImportError(node, name, str(e))
    del module
    return module_dict


def import_from(
    node: ast.ImportFrom, script_directory: Path, ignore_names: list[str] = ()
) -> dict[str, tp.Any]:
    """Import names into given namespace dictionary."""
    if node.module in ignore_names:
        return {}
    try:
        # Try to import and reload module normally.
        module = importlib.import_module(node.module)
        importlib.reload(module)
    except ImportError:
        # Try to import module on path.
        if script_directory is None:
            raise EVSImportError(
                node,
                node.module,
                "`script_directory` needed for relative import, but was not given to `EVSParser` or auto-detected.",
            )
        level = 0 if node.level == 0 else node.level - 1  # single dot (level 1) is the same as no dot (level 0)
        module_path = (script_directory / ("../" * level + node.module.replace(".", "/") + ".py")).resolve()
        if not module_path.is_file():
            raise EVSImportError(node, node.module, f"Cannot import missing module file: {module_path}")
        try:
            module = import_arbitrary_module(module_path)
        except ImportError as ex:
            if "no known parent package" in str(ex):
                raise EVSImportError(
                    node,
                    node.module,
                    f"Cannot import module '{module_path}' due to having no known parent package.\n"
                    f"    Note that currently, EVS files cannot import modules that "
                    f"contain their own relative imports. Please use absolute imports only."
                )
            raise

    module_dict = {}
    for alias in node.names:
        name = alias.name
        if name in ignore_names:
            continue  # already imported
        if name == "*":
            if "__all__" in vars(module):
                all_names = vars(module)["__all__"]
            else:
                # Get all names that were defined in the module and don't begin with an underscore.
                module_name = node.module.split(".")[-1]  # `__module__` is name-only in certain contexts I think
                all_names = [
                    n
                    for n, attr in vars(module).items()
                    if not n.startswith("_") and (
                        not hasattr(attr, "__module__") or attr.__module__ in (node.module, module_name)
                    )
                ]
            for name_ in all_names:
                try:
                    module_dict[name_] = getattr(module, name_)
                except AttributeError as e:
                    _LOGGER.error(
                        f"EVS error: could not import {name_} from module {node.module} " f"(__all__ = {all_names})"
                    )
                    raise EVSImportFromError(node, node.module, name_, str(e))
        else:
            as_name = alias.asname if alias.asname is not None else name
            try:
                module_dict[as_name] = getattr(module, name)
            except AttributeError as e:
                raise EVSImportFromError(node, node.module, name, str(e))
    del module
    return module_dict


def import_from_common_func(
    module_name: str, namespace: dict, script_directory: Path, names: list[str], level: int
):
    """Import names into given namespace dictionary."""
    try:
        # Try to import and reload module normally.
        module = importlib.import_module(module_name)
        importlib.reload(module)
    except ImportError:
        # Try to import module on path.
        if script_directory is None:
            raise EVSCommonFuncImportError(
                module_name,
                "",
                "`script_directory` needed for relative import, but was not given to `EVSParser` or be detected.",
            )
        module_path = script_directory / ("../" * level + module_name.replace(".", "/") + ".py")
        if not module_path.is_file():
            raise EVSCommonFuncImportError(module_name, "", "Cannot import missing module file.")
        module = import_arbitrary_module(module_path)

    for name in names:
        if name == "*":
            raise EVSCommonFuncImportError(module_name, "", "Cannot star import from COMMON_FUNC module.")
        try:
            namespace[name] = getattr(module, name)
        except AttributeError as ex:
            raise EVSCommonFuncImportError(module_name, name, str(ex))
    del module


def define_args(arg_types: str) -> list[tuple[int, int]]:
    """Converts an argument format string (e.g. `"iIIfB"`) to a list of `(write_offset, size)` tuples, usually for
    generating `EventArgRepl` instances."""
    args = []
    for i, c in enumerate(arg_types):
        if c in "Bb":
            c_size = 1
        elif c in "Hh":
            c_size = 2
        elif c in "Iif":
            c_size = 4
        else:
            raise ValueError(f"Invalid format character '{c}' in `arg_types`.")
        args.append((get_write_offset(arg_types, i), c_size))
    return args


def as_event_statement_node(node: ast.stmt, msg="") -> EventStatementTyping:
    """Intellisense hack to check and validate node type."""
    if not isinstance(node, (ast.Expr, ast.For, ast.If, ast.Assign, ast.Return)):
        raise EVSSyntaxError(node, msg or f"Invalid Event Statement node: {ast.dump(node)}")
    return node


def as_condition_node(node: ast.expr, msg="") -> ConditionNodeTyping:
    """Intellisense hack to check and validate node type."""
    if not isinstance(node, (ast.UnaryOp, ast.BoolOp, ast.Compare, ast.Name, ast.Attribute, ast.Call)):
        raise EVSSyntaxError(node, msg or f"Invalid Condition node: {ast.dump(node)}")
    return node


def as_skip_return_node(node: ast.expr, msg="") -> SkipReturnTyping:
    """Intellisense hack to check and validate node type."""
    if not isinstance(node, (ast.UnaryOp, ast.Name, ast.Attribute, ast.Compare, ast.Call)):
        raise EVSSyntaxError(node, msg or f"Invalid Skip/Return node: {ast.dump(node)}")
    return node


def no_skip_or_negate_or_return(func):
    @wraps(func)
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrReturnError
        if negate:
            raise NoNegateError
        if end_event or restart_event:
            raise NoSkipOrReturnError
        if condition is None:
            raise ValueError("Condition index must be specified.")
        return func(*args, condition=condition, **kwargs)

    return decorated


def negate_only(func):
    @wraps(func)
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrReturnError
        if end_event or restart_event:
            raise NoSkipOrReturnError
        if condition is None:
            raise ValueError("Condition index must be specified.")
        return func(*args, condition=condition, negate=negate, **kwargs)

    return decorated


def skip_and_negate_and_return(func):
    @wraps(func)
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, skip_lines=skip_lines, negate=negate, **kwargs)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, condition=condition, negate=negate, **kwargs)

        if end_event:
            if restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, end_event=True, negate=negate, **kwargs)

        if restart_event:
            return func(*args, restart_event=True, negate=negate, **kwargs)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")

    return decorated
