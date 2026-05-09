# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SearchQueryResponse"]


class SearchQueryResponse(BaseModel):
    capture_id: str = FieldInfo(alias="captureId")

    content: str
