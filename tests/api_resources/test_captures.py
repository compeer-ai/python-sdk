# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from barque import Barque, AsyncBarque
from tests.utils import assert_matches_type
from barque.types import CaptureCreateResponse, CaptureSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCaptures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Barque) -> None:
        capture = client.captures.create(
            content="content",
            project_id="projectId",
            type="text",
        )
        assert_matches_type(CaptureCreateResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Barque) -> None:
        response = client.captures.with_raw_response.create(
            content="content",
            project_id="projectId",
            type="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capture = response.parse()
        assert_matches_type(CaptureCreateResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Barque) -> None:
        with client.captures.with_streaming_response.create(
            content="content",
            project_id="projectId",
            type="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capture = response.parse()
            assert_matches_type(CaptureCreateResponse, capture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Barque) -> None:
        capture = client.captures.search(
            project_id="projectId",
            query="query",
        )
        assert_matches_type(CaptureSearchResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Barque) -> None:
        response = client.captures.with_raw_response.search(
            project_id="projectId",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capture = response.parse()
        assert_matches_type(CaptureSearchResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Barque) -> None:
        with client.captures.with_streaming_response.search(
            project_id="projectId",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capture = response.parse()
            assert_matches_type(CaptureSearchResponse, capture, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCaptures:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBarque) -> None:
        capture = await async_client.captures.create(
            content="content",
            project_id="projectId",
            type="text",
        )
        assert_matches_type(CaptureCreateResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBarque) -> None:
        response = await async_client.captures.with_raw_response.create(
            content="content",
            project_id="projectId",
            type="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capture = await response.parse()
        assert_matches_type(CaptureCreateResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBarque) -> None:
        async with async_client.captures.with_streaming_response.create(
            content="content",
            project_id="projectId",
            type="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capture = await response.parse()
            assert_matches_type(CaptureCreateResponse, capture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncBarque) -> None:
        capture = await async_client.captures.search(
            project_id="projectId",
            query="query",
        )
        assert_matches_type(CaptureSearchResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncBarque) -> None:
        response = await async_client.captures.with_raw_response.search(
            project_id="projectId",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capture = await response.parse()
        assert_matches_type(CaptureSearchResponse, capture, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncBarque) -> None:
        async with async_client.captures.with_streaming_response.search(
            project_id="projectId",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capture = await response.parse()
            assert_matches_type(CaptureSearchResponse, capture, path=["response"])

        assert cast(Any, response.is_closed) is True
