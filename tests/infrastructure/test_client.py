import os

import httpx
import pytest
import respx

from se.infrastructure.http_client import HttpClient

BASE_URL = os.getenv('PRESENTATION_SERVICE_URL', 'base_url_error')
URL_PATH = '/presentation/'
TEST_URL = BASE_URL + URL_PATH


# Fixtures


@pytest.fixture
def http_client() -> HttpClient:
    client = HttpClient()
    return client


# Tests


@pytest.mark.respx(base_url=BASE_URL)
def test_http_client_status_204(
    respx_mock: respx.MockRouter,
    http_client: httpx.Client,
) -> None:
    respx_mock.get(URL_PATH).mock(return_value=httpx.Response(204))
    response = http_client.get(TEST_URL)
    assert response.status_code == 204


@pytest.mark.respx(base_url=BASE_URL)
def test_http_client_status_404(
    respx_mock: respx.MockRouter,
    http_client: httpx.Client,
) -> None:
    respx_mock.get('/presentation/').mock(return_value=httpx.Response(404))
    response = http_client.get(TEST_URL)
    assert response.status_code == 404
