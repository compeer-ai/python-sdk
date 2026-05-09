# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from compeer import Compeer, AsyncCompeer
from tests.utils import assert_matches_type
from compeer.types import CaptureCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCapture:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Compeer) -> None:
        capture = client.capture.create(
            workspace="workspace",
            content="content",
            store="store",
            type="text",
        )
        assert_matches_type(CaptureCreateResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Compeer) -> None:
        response = client.capture.with_raw_response.create(
            workspace="workspace",
            content="content",
            store="store",
            type="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capture = response.parse()
        assert_matches_type(CaptureCreateResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Compeer) -> None:
        with client.capture.with_streaming_response.create(
            workspace="workspace",
            content="content",
            store="store",
            type="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capture = response.parse()
            assert_matches_type(CaptureCreateResponse, capture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Compeer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace` but received ''"):
            client.capture.with_raw_response.create(
                workspace="",
                content="content",
                store="store",
                type="text",
            )


class TestAsyncCapture:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCompeer) -> None:
        capture = await async_client.capture.create(
            workspace="workspace",
            content="content",
            store="store",
            type="text",
        )
        assert_matches_type(CaptureCreateResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCompeer) -> None:
        response = await async_client.capture.with_raw_response.create(
            workspace="workspace",
            content="content",
            store="store",
            type="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capture = await response.parse()
        assert_matches_type(CaptureCreateResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCompeer) -> None:
        async with async_client.capture.with_streaming_response.create(
            workspace="workspace",
            content="content",
            store="store",
            type="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capture = await response.parse()
            assert_matches_type(CaptureCreateResponse, capture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCompeer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace` but received ''"):
            await async_client.capture.with_raw_response.create(
                workspace="",
                content="content",
                store="store",
                type="text",
            )
