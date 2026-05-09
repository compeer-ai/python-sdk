# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["WorkspaceListResponse", "WorkspaceListResponseItem"]


class WorkspaceListResponseItem(BaseModel):
    id: str

    name: str


WorkspaceListResponse: TypeAlias = List[WorkspaceListResponseItem]
