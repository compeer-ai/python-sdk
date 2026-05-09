# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StoreListResponse"]


class StoreListResponse(BaseModel):
    id: str

    description: Optional[str] = None

    name: str

    workspace_id: str = FieldInfo(alias="workspaceId")
