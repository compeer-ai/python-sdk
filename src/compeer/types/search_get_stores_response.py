# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SearchGetStoresResponse"]


class SearchGetStoresResponse(BaseModel):
    capture_id: str = FieldInfo(alias="captureId")

    content: str
