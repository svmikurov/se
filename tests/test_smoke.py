import pytest
from playwright.sync_api import Page


@pytest.mark.e2e
def test_admin_is_reachable(page: Page, base_url: str) -> None:
    response = page.goto(base_url)
    assert response is not None
    assert response.ok, f'expected 2xx, got {response.status}'


@pytest.mark.e2e
def test_admin_login_form_present(page: Page, base_url: str) -> None:
    page.goto(f'{base_url}/admin/login/')
    assert page.locator('input[name="username"]').is_visible()
    assert page.locator('input[name="password"]').is_visible()
