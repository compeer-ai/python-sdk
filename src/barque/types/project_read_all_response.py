# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectReadAllResponse", "ProjectReadAllResponseItem"]


class ProjectReadAllResponseItem(BaseModel):
    id: str

    name: str

    user_id: str = FieldInfo(alias="userId")


ProjectReadAllResponse: TypeAlias = List[ProjectReadAllResponseItem]
