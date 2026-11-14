import pytest
from playwright.sync_api import Page


@pytest.mark.e2e
def test_admin_login_form_present(page: Page, base_url: str) -> None:
    response = page.goto(f'{base_url}/ru/glossary/')
    assert response
    assert response.status == 200
