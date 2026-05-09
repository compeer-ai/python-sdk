# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from compeer import Compeer, AsyncCompeer
from tests.utils import assert_matches_type
from compeer.types import OidcRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOidc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Compeer) -> None:
        oidc = client.oidc.retrieve()
        assert_matches_type(OidcRetrieveResponse, oidc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Compeer) -> None:
        response = client.oidc.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oidc = response.parse()
        assert_matches_type(OidcRetrieveResponse, oidc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Compeer) -> None:
        with client.oidc.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oidc = response.parse()
            assert_matches_type(OidcRetrieveResponse, oidc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOidc:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCompeer) -> None:
        oidc = await async_client.oidc.retrieve()
        assert_matches_type(OidcRetrieveResponse, oidc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCompeer) -> None:
        response = await async_client.oidc.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oidc = await response.parse()
        assert_matches_type(OidcRetrieveResponse, oidc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCompeer) -> None:
        async with async_client.oidc.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oidc = await response.parse()
            assert_matches_type(OidcRetrieveResponse, oidc, path=["response"])

        assert cast(Any, response.is_closed) is True
