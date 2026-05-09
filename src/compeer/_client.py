# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import alive, search, stores, capture, workspaces
    from .resources.alive import AliveResource, AsyncAliveResource
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.stores import StoresResource, AsyncStoresResource
    from .resources.capture import CaptureResource, AsyncCaptureResource
    from .resources.workspaces import WorkspacesResource, AsyncWorkspacesResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Compeer", "AsyncCompeer", "Client", "AsyncClient"]


class Compeer(SyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Compeer client instance.

        This automatically infers the `api_key` argument from the `COMPEER_APIKEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COMPEER_APIKEY")
        self.api_key = api_key

        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("COMPEER_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:3000/api/v1"

        custom_headers_env = os.environ.get("COMPEER_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def alive(self) -> AliveResource:
        from .resources.alive import AliveResource

        return AliveResource(self)

    @cached_property
    def stores(self) -> StoresResource:
        from .resources.stores import StoresResource

        return StoresResource(self)

    @cached_property
    def search(self) -> SearchResource:
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def workspaces(self) -> WorkspacesResource:
        from .resources.workspaces import WorkspacesResource

        return WorkspacesResource(self)

    @cached_property
    def capture(self) -> CaptureResource:
        from .resources.capture import CaptureResource

        return CaptureResource(self)

    @cached_property
    def with_raw_response(self) -> CompeerWithRawResponse:
        return CompeerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompeerWithStreamedResponse:
        return CompeerWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
            **(self._api_key_auth if security.get("api_key_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-Api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        if headers.get("X-Api-key") or isinstance(custom_headers.get("X-Api-key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either bearer_token or api_key to be set. Or for one of the `Authorization` or `X-Api-key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCompeer(AsyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCompeer client instance.

        This automatically infers the `api_key` argument from the `COMPEER_APIKEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COMPEER_APIKEY")
        self.api_key = api_key

        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("COMPEER_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:3000/api/v1"

        custom_headers_env = os.environ.get("COMPEER_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def alive(self) -> AsyncAliveResource:
        from .resources.alive import AsyncAliveResource

        return AsyncAliveResource(self)

    @cached_property
    def stores(self) -> AsyncStoresResource:
        from .resources.stores import AsyncStoresResource

        return AsyncStoresResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def workspaces(self) -> AsyncWorkspacesResource:
        from .resources.workspaces import AsyncWorkspacesResource

        return AsyncWorkspacesResource(self)

    @cached_property
    def capture(self) -> AsyncCaptureResource:
        from .resources.capture import AsyncCaptureResource

        return AsyncCaptureResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncCompeerWithRawResponse:
        return AsyncCompeerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompeerWithStreamedResponse:
        return AsyncCompeerWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
            **(self._api_key_auth if security.get("api_key_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-Api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        if headers.get("X-Api-key") or isinstance(custom_headers.get("X-Api-key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either bearer_token or api_key to be set. Or for one of the `Authorization` or `X-Api-key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CompeerWithRawResponse:
    _client: Compeer

    def __init__(self, client: Compeer) -> None:
        self._client = client

    @cached_property
    def alive(self) -> alive.AliveResourceWithRawResponse:
        from .resources.alive import AliveResourceWithRawResponse

        return AliveResourceWithRawResponse(self._client.alive)

    @cached_property
    def stores(self) -> stores.StoresResourceWithRawResponse:
        from .resources.stores import StoresResourceWithRawResponse

        return StoresResourceWithRawResponse(self._client.stores)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def workspaces(self) -> workspaces.WorkspacesResourceWithRawResponse:
        from .resources.workspaces import WorkspacesResourceWithRawResponse

        return WorkspacesResourceWithRawResponse(self._client.workspaces)

    @cached_property
    def capture(self) -> capture.CaptureResourceWithRawResponse:
        from .resources.capture import CaptureResourceWithRawResponse

        return CaptureResourceWithRawResponse(self._client.capture)


class AsyncCompeerWithRawResponse:
    _client: AsyncCompeer

    def __init__(self, client: AsyncCompeer) -> None:
        self._client = client

    @cached_property
    def alive(self) -> alive.AsyncAliveResourceWithRawResponse:
        from .resources.alive import AsyncAliveResourceWithRawResponse

        return AsyncAliveResourceWithRawResponse(self._client.alive)

    @cached_property
    def stores(self) -> stores.AsyncStoresResourceWithRawResponse:
        from .resources.stores import AsyncStoresResourceWithRawResponse

        return AsyncStoresResourceWithRawResponse(self._client.stores)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def workspaces(self) -> workspaces.AsyncWorkspacesResourceWithRawResponse:
        from .resources.workspaces import AsyncWorkspacesResourceWithRawResponse

        return AsyncWorkspacesResourceWithRawResponse(self._client.workspaces)

    @cached_property
    def capture(self) -> capture.AsyncCaptureResourceWithRawResponse:
        from .resources.capture import AsyncCaptureResourceWithRawResponse

        return AsyncCaptureResourceWithRawResponse(self._client.capture)


class CompeerWithStreamedResponse:
    _client: Compeer

    def __init__(self, client: Compeer) -> None:
        self._client = client

    @cached_property
    def alive(self) -> alive.AliveResourceWithStreamingResponse:
        from .resources.alive import AliveResourceWithStreamingResponse

        return AliveResourceWithStreamingResponse(self._client.alive)

    @cached_property
    def stores(self) -> stores.StoresResourceWithStreamingResponse:
        from .resources.stores import StoresResourceWithStreamingResponse

        return StoresResourceWithStreamingResponse(self._client.stores)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def workspaces(self) -> workspaces.WorkspacesResourceWithStreamingResponse:
        from .resources.workspaces import WorkspacesResourceWithStreamingResponse

        return WorkspacesResourceWithStreamingResponse(self._client.workspaces)

    @cached_property
    def capture(self) -> capture.CaptureResourceWithStreamingResponse:
        from .resources.capture import CaptureResourceWithStreamingResponse

        return CaptureResourceWithStreamingResponse(self._client.capture)


class AsyncCompeerWithStreamedResponse:
    _client: AsyncCompeer

    def __init__(self, client: AsyncCompeer) -> None:
        self._client = client

    @cached_property
    def alive(self) -> alive.AsyncAliveResourceWithStreamingResponse:
        from .resources.alive import AsyncAliveResourceWithStreamingResponse

        return AsyncAliveResourceWithStreamingResponse(self._client.alive)

    @cached_property
    def stores(self) -> stores.AsyncStoresResourceWithStreamingResponse:
        from .resources.stores import AsyncStoresResourceWithStreamingResponse

        return AsyncStoresResourceWithStreamingResponse(self._client.stores)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def workspaces(self) -> workspaces.AsyncWorkspacesResourceWithStreamingResponse:
        from .resources.workspaces import AsyncWorkspacesResourceWithStreamingResponse

        return AsyncWorkspacesResourceWithStreamingResponse(self._client.workspaces)

    @cached_property
    def capture(self) -> capture.AsyncCaptureResourceWithStreamingResponse:
        from .resources.capture import AsyncCaptureResourceWithStreamingResponse

        return AsyncCaptureResourceWithStreamingResponse(self._client.capture)


Client = Compeer

AsyncClient = AsyncCompeer
