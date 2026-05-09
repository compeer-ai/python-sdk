# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from compeer import Compeer, AsyncCompeer
from tests.utils import assert_matches_type
from compeer.types import BackupRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBackup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Compeer) -> None:
        backup = client.backup.retrieve()
        assert_matches_type(BackupRetrieveResponse, backup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Compeer) -> None:
        response = client.backup.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = response.parse()
        assert_matches_type(BackupRetrieveResponse, backup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Compeer) -> None:
        with client.backup.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = response.parse()
            assert_matches_type(BackupRetrieveResponse, backup, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBackup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCompeer) -> None:
        backup = await async_client.backup.retrieve()
        assert_matches_type(BackupRetrieveResponse, backup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCompeer) -> None:
        response = await async_client.backup.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backup = await response.parse()
        assert_matches_type(BackupRetrieveResponse, backup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCompeer) -> None:
        async with async_client.backup.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backup = await response.parse()
            assert_matches_type(BackupRetrieveResponse, backup, path=["response"])

        assert cast(Any, response.is_closed) is True
