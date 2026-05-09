# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import capture_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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

__all__ = ["CaptureResource", "AsyncCaptureResource"]


class CaptureResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CaptureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/barque-python#accessing-raw-response-data-eg-headers
        """
        return CaptureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CaptureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/barque-python#with_streaming_response
        """
        return CaptureResourceWithStreamingResponse(self)

    def create(
        self,
        workspace: str,
        *,
        content: str,
        store: str,
        type: Literal["text", "data", "url"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureCreateResponse:
        """
        Create a capture

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace:
            raise ValueError(f"Expected a non-empty value for `workspace` but received {workspace!r}")
        return self._post(
            path_template("/{workspace}/capture", workspace=workspace),
            body=maybe_transform(
                {
                    "content": content,
                    "store": store,
                    "type": type,
                },
                capture_create_params.CaptureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureCreateResponse,
        )


class AsyncCaptureResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCaptureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/barque-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCaptureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCaptureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/barque-python#with_streaming_response
        """
        return AsyncCaptureResourceWithStreamingResponse(self)

    async def create(
        self,
        workspace: str,
        *,
        content: str,
        store: str,
        type: Literal["text", "data", "url"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaptureCreateResponse:
        """
        Create a capture

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace:
            raise ValueError(f"Expected a non-empty value for `workspace` but received {workspace!r}")
        return await self._post(
            path_template("/{workspace}/capture", workspace=workspace),
            body=await async_maybe_transform(
                {
                    "content": content,
                    "store": store,
                    "type": type,
                },
                capture_create_params.CaptureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaptureCreateResponse,
        )


class CaptureResourceWithRawResponse:
    def __init__(self, capture: CaptureResource) -> None:
        self._capture = capture

        self.create = to_raw_response_wrapper(
            capture.create,
        )


class AsyncCaptureResourceWithRawResponse:
    def __init__(self, capture: AsyncCaptureResource) -> None:
        self._capture = capture

        self.create = async_to_raw_response_wrapper(
            capture.create,
        )


class CaptureResourceWithStreamingResponse:
    def __init__(self, capture: CaptureResource) -> None:
        self._capture = capture

        self.create = to_streamed_response_wrapper(
            capture.create,
        )


class AsyncCaptureResourceWithStreamingResponse:
    def __init__(self, capture: AsyncCaptureResource) -> None:
        self._capture = capture

        self.create = async_to_streamed_response_wrapper(
            capture.create,
        )
