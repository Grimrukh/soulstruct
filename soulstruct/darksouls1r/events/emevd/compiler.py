"""Contains additional custom instructions (by me) that wrap other real EMEVD instructions.

Though you may "call" these functions in EVS script, they are never actually called directly. The three dictionaries
defined at the top of the module (filled by decorators at module load) will be used to look up the functions. When
compiling EVS, the dictionary will be reversed and the EVS instruction name will be used to look up a custom instruction
from this module or the (category, index) for EMEDF. When decompiling to EVS,

Usually, these just combine multiple underlying EMEVD instructions into one (e.g., `IfActionButton`).

NOTE: This file is basically identical to the PTDE version, but needs to be redefined for the DSR `COMPILER`.
"""
from __future__ import annotations

__all__ = [
    "EVSInstructionCompiler",
]

import logging

from soulstruct.darksouls1ptde.events.emevd.compiler import EVSInstructionCompiler as _BasePTDECompiler

from .emedf import EMEDF_ALIASES


_LOGGER = logging.getLogger(__name__)


class EVSInstructionCompiler(_BasePTDECompiler):
    """Same custom instructions as PTDE."""

    EMEDF_ALIASES = EMEDF_ALIASES


EVSInstructionCompiler.process_custom_instructions()
