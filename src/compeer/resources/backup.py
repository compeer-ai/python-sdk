# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.backup_retrieve_response import BackupRetrieveResponse

__all__ = ["BackupResource", "AsyncBackupResource"]


class BackupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BackupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/barque-python#accessing-raw-response-data-eg-headers
        """
        return BackupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BackupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/barque-python#with_streaming_response
        """
        return BackupResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BackupRetrieveResponse:
        """Get a workspace's stores"""
        return self._get(
            "/backup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BackupRetrieveResponse,
        )


class AsyncBackupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBackupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/barque-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBackupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBackupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/barque-python#with_streaming_response
        """
        return AsyncBackupResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BackupRetrieveResponse:
        """Get a workspace's stores"""
        return await self._get(
            "/backup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BackupRetrieveResponse,
        )


class BackupResourceWithRawResponse:
    def __init__(self, backup: BackupResource) -> None:
        self._backup = backup

        self.retrieve = to_raw_response_wrapper(
            backup.retrieve,
        )


class AsyncBackupResourceWithRawResponse:
    def __init__(self, backup: AsyncBackupResource) -> None:
        self._backup = backup

        self.retrieve = async_to_raw_response_wrapper(
            backup.retrieve,
        )


class BackupResourceWithStreamingResponse:
    def __init__(self, backup: BackupResource) -> None:
        self._backup = backup

        self.retrieve = to_streamed_response_wrapper(
            backup.retrieve,
        )


class AsyncBackupResourceWithStreamingResponse:
    def __init__(self, backup: AsyncBackupResource) -> None:
        self._backup = backup

        self.retrieve = async_to_streamed_response_wrapper(
            backup.retrieve,
        )
