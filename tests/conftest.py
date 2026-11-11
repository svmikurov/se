import os
from typing import Any, Generator

import pytest
from playwright.sync_api import Browser, sync_playwright

TEST_RESULTS_DIR = os.environ.get('TEST_RESULTS_DIR', 'test-results')


def pytest_configure(config: dict[str, Any]) -> None:
    os.makedirs(TEST_RESULTS_DIR, exist_ok=True)


@pytest.fixture(scope='session')
def base_url() -> str:
    return os.environ.get('BASE_URL', 'http://admin:8100')


@pytest.fixture(scope='session')
def browser() -> Generator[Browser, None, None]:
    headless = os.environ.get('HEADLESS', '1') == '1'
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()


# FIXME: Fix type ignore
@pytest.fixture()
def page(browser, request):  # type: ignore[no-untyped-def]
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page

    failed = (
        getattr(request.node, 'rep_call', None)
        and request.node.rep_call.failed
    )
    if failed:
        name = request.node.name.replace('/', '_')
        page.screenshot(path=f'{TEST_RESULTS_DIR}/{name}.png', full_page=True)
        context.tracing.stop(path=f'{TEST_RESULTS_DIR}/{name}.zip')
    else:
        context.tracing.stop()

    context.close()


# FIXME: Fix type ignore
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):  # type: ignore[no-untyped-def]
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)
