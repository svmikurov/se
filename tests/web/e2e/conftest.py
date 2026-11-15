import os

import pytest

TEST_RESULTS_DIR = os.environ.get('TEST_RESULTS_DIR', 'test-results')

WEB_SERVICE_SCHEME = 'http://web:8200'


@pytest.fixture(scope='session')
def base_url() -> str:
    return os.environ.get('BASE_URL', WEB_SERVICE_SCHEME)
