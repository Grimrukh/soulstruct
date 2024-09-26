from __future__ import annotations

__all__ = ["NVMBND"]

from dataclasses import dataclass

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.dcx import DCXType
from soulstruct.base.maps.navmesh import BaseNVMBND


@dataclass(slots=True)
class NVMBND(BaseNVMBND):
    """Manage `NVM` entries in a Binder."""

    # Override defaults.
    version: BinderVersion = BinderVersion.V3
    v4_info: BinderVersion4Info | None = None
    dcx_type: DCXType = DCXType.Null
