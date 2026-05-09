# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CaptureSearchResponse", "CaptureSearchResponseItem"]


class CaptureSearchResponseItem(BaseModel):
    capture_id: str = FieldInfo(alias="captureId")

    content: str

    percentage_match: float = FieldInfo(alias="percentageMatch")


CaptureSearchResponse: TypeAlias = List[CaptureSearchResponseItem]
