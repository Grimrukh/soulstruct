"""Handlers for FromSoft compression format, `DCX`.

NOTE: The C++ library ``Firelink``, with Python bindings ``pyrelink``, should largely replace this submodule.
``pyrelink`` is significantly faster and offers the same methods.
"""
from .core import DCXType, compress, decompress, is_dcx
