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
from ..types.oidc_retrieve_response import OidcRetrieveResponse

__all__ = ["OidcResource", "AsyncOidcResource"]


class OidcResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OidcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/barque-python#accessing-raw-response-data-eg-headers
        """
        return OidcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OidcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/barque-python#with_streaming_response
        """
        return OidcResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OidcRetrieveResponse:
        """Get a workspace's stores"""
        return self._get(
            "/oidc",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OidcRetrieveResponse,
        )


class AsyncOidcResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOidcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/barque-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOidcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOidcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/barque-python#with_streaming_response
        """
        return AsyncOidcResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OidcRetrieveResponse:
        """Get a workspace's stores"""
        return await self._get(
            "/oidc",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OidcRetrieveResponse,
        )


class OidcResourceWithRawResponse:
    def __init__(self, oidc: OidcResource) -> None:
        self._oidc = oidc

        self.retrieve = to_raw_response_wrapper(
            oidc.retrieve,
        )


class AsyncOidcResourceWithRawResponse:
    def __init__(self, oidc: AsyncOidcResource) -> None:
        self._oidc = oidc

        self.retrieve = async_to_raw_response_wrapper(
            oidc.retrieve,
        )


class OidcResourceWithStreamingResponse:
    def __init__(self, oidc: OidcResource) -> None:
        self._oidc = oidc

        self.retrieve = to_streamed_response_wrapper(
            oidc.retrieve,
        )


class AsyncOidcResourceWithStreamingResponse:
    def __init__(self, oidc: AsyncOidcResource) -> None:
        self._oidc = oidc

        self.retrieve = async_to_streamed_response_wrapper(
            oidc.retrieve,
        )
