from __future__ import annotations

__all__ = ["GameParamBND"]

import logging
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.dcx import DCXType
from soulstruct.base.params.gameparambnd import GameParamBND as _BaseGameParamBND
from soulstruct.utilities.files import SOULSTRUCT_PATH
from soulstruct.utilities.ParamCrypt import ParamCrypt

from . import paramdef

_LOGGER = logging.getLogger(__name__)

# if tp.TYPE_CHECKING:
#     from ..text.msg_directory import MSGDirectory


class GameParamBND(_BaseGameParamBND):

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = "N:\\GR\\data\\Param\\param\\GameParam"
    PARAMDEF_MODULE: tp.ClassVar = paramdef

    signature: str = "10811000"
    dcx_type: DCXType = DCXType.DCX_DFLT_11000_44_9_15  # NOTE: This is NOT the standard `KRAK` Elden Ring compression.
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=lambda: BinderVersion4Info(hash_table_type=4))

    @classmethod
    def from_encrypted_path(cls, encrypted_path: Path | str) -> tp.Self:
        """Load `GameParamBND` from encrypted DCX-compressed Binder, generally `regulation.bin`."""
        encrypted_path = Path(encrypted_path)
        temp_decrypted = SOULSTRUCT_PATH("__ParamCrypt__.parambnd.dcx")
        _LOGGER.info(f"Decrypting Elden Ring `GameParamBND` from regulation: {encrypted_path}")
        ParamCrypt(encrypted_path, "decrypt", "er", temp_decrypted)
        data = Path(temp_decrypted).read_bytes()  # DCX-compressed `Binder` (BND4)
        temp_decrypted.unlink()
        gameparambnd = cls.from_bytes(data)
        gameparambnd.path = encrypted_path
        return gameparambnd

    def write_encrypted(self, file_path: None | str | Path = None, make_dirs=True):
        """Write back to encrypted, game-ready encrypted file, generally `regulation.bin`."""
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because file default `path` has not been set.")
            file_path = self.path.parent / "regulation.bin"
        else:
            file_path = Path(file_path)

        if make_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)

        temp_decrypted = SOULSTRUCT_PATH("__ParamCrypt__.parambnd.dcx")
        self.write(temp_decrypted, make_dirs=False, check_hash=False)
        ParamCrypt(temp_decrypted, "encrypt", "er", file_path)
        # temp_decrypted.unlink()

    # TODO: `rename_entries_from_text` and other utilities


def examine_er_params():

    from soulstruct.base.params.param import Param, TypedParam
    from soulstruct.base.params.param_dict import ParamDict
    from soulstruct.config import ELDEN_RING_PATH
    from soulstruct.eldenring.params import paramdef

    reg = GameParamBND.from_encrypted_path(ELDEN_RING_PATH / "regulation.bin")
    for entry in reg.entries:
        param_type = Param.detect_param_type(entry.data)
        try:
            data_type = getattr(paramdef, param_type)
        except AttributeError:
            # Fall back to `ParamDict` (with no `ParamDef`).
            param = entry.to_binary_file(ParamDict)
            print(f"{entry.name} read as a ParamDict.")
        else:
            param = entry.to_binary_file(TypedParam(data_type))
            print(f"{entry.name} read successfully.")


if __name__ == '__main__':
    examine_er_params()
