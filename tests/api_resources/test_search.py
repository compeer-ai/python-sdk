# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from compeer import Compeer, AsyncCompeer
from tests.utils import assert_matches_type
from compeer.types import SearchGetStoresResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_stores(self, client: Compeer) -> None:
        search = client.search.get_stores(
            workspace="workspace",
            query="query",
        )
        assert_matches_type(SearchGetStoresResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_stores_with_all_params(self, client: Compeer) -> None:
        search = client.search.get_stores(
            workspace="workspace",
            query="query",
            store="store",
        )
        assert_matches_type(SearchGetStoresResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_stores(self, client: Compeer) -> None:
        response = client.search.with_raw_response.get_stores(
            workspace="workspace",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchGetStoresResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_stores(self, client: Compeer) -> None:
        with client.search.with_streaming_response.get_stores(
            workspace="workspace",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchGetStoresResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_stores(self, client: Compeer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace` but received ''"):
            client.search.with_raw_response.get_stores(
                workspace="",
                query="query",
            )


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_stores(self, async_client: AsyncCompeer) -> None:
        search = await async_client.search.get_stores(
            workspace="workspace",
            query="query",
        )
        assert_matches_type(SearchGetStoresResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_stores_with_all_params(self, async_client: AsyncCompeer) -> None:
        search = await async_client.search.get_stores(
            workspace="workspace",
            query="query",
            store="store",
        )
        assert_matches_type(SearchGetStoresResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_stores(self, async_client: AsyncCompeer) -> None:
        response = await async_client.search.with_raw_response.get_stores(
            workspace="workspace",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchGetStoresResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_stores(self, async_client: AsyncCompeer) -> None:
        async with async_client.search.with_streaming_response.get_stores(
            workspace="workspace",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchGetStoresResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_stores(self, async_client: AsyncCompeer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace` but received ''"):
            await async_client.search.with_raw_response.get_stores(
                workspace="",
                query="query",
            )
