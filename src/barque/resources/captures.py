# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import capture_create_params, capture_search_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.capture_create_response import CaptureCreateResponse
from ..types.capture_search_response import CaptureSearchResponse

__all__ = ["CapturesResource", "AsyncCapturesResource"]


class CapturesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CapturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/barque-python#accessing-raw-response-data-eg-headers
        """
        return CapturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CapturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/barque-python#with_streaming_response
        """
        return CapturesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content: str,
        project_id: str,
        type: Literal["text", "data", "url"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureCreateResponse:
        """
        Create a new text, data, or URL capture in a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/capture",
            body=maybe_transform(
                {
                    "content": content,
                    "project_id": project_id,
                    "type": type,
                },
                capture_create_params.CaptureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureCreateResponse,
        )

    def search(
        self,
        *,
        project_id: str,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureSearchResponse:
        """
        Search for captures within a project using semantic search

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "project_id": project_id,
                        "query": query,
                    },
                    capture_search_params.CaptureSearchParams,
                ),
            ),
            cast_to=CaptureSearchResponse,
        )


class AsyncCapturesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCapturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/barque-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCapturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCapturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/barque-python#with_streaming_response
        """
        return AsyncCapturesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content: str,
        project_id: str,
        type: Literal["text", "data", "url"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureCreateResponse:
        """
        Create a new text, data, or URL capture in a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/capture",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "project_id": project_id,
                    "type": type,
                },
                capture_create_params.CaptureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureCreateResponse,
        )

    async def search(
        self,
        *,
        project_id: str,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureSearchResponse:
        """
        Search for captures within a project using semantic search

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "project_id": project_id,
                        "query": query,
                    },
                    capture_search_params.CaptureSearchParams,
                ),
            ),
            cast_to=CaptureSearchResponse,
        )


class CapturesResourceWithRawResponse:
    def __init__(self, captures: CapturesResource) -> None:
        self._captures = captures

        self.create = to_raw_response_wrapper(
            captures.create,
        )
        self.search = to_raw_response_wrapper(
            captures.search,
        )


class AsyncCapturesResourceWithRawResponse:
    def __init__(self, captures: AsyncCapturesResource) -> None:
        self._captures = captures

        self.create = async_to_raw_response_wrapper(
            captures.create,
        )
        self.search = async_to_raw_response_wrapper(
            captures.search,
        )


class CapturesResourceWithStreamingResponse:
    def __init__(self, captures: CapturesResource) -> None:
        self._captures = captures

        self.create = to_streamed_response_wrapper(
            captures.create,
        )
        self.search = to_streamed_response_wrapper(
            captures.search,
        )


class AsyncCapturesResourceWithStreamingResponse:
    def __init__(self, captures: AsyncCapturesResource) -> None:
        self._captures = captures

        self.create = async_to_streamed_response_wrapper(
            captures.create,
        )
        self.search = async_to_streamed_response_wrapper(
            captures.search,
        )
