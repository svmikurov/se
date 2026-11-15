from urllib.parse import urljoin

import pytest
from playwright.sync_api import Page, Response, expect


class BasePage:
    path: str = ''
    title: str = ''

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, base_url: str) -> Response:
        url = urljoin(base_url, self.path)
        response = self.page.goto(url)
        assert response is not None, f'No response from {url}'
        return response


class GlossaryPage(BasePage):
    path = '/glossary/'
    title = 'Глоссарий'


@pytest.mark.e2e
def test_that_glossary_index_page_has_title(page: Page, base_url: str) -> None:
    page_obj = GlossaryPage(page)
    page_obj.navigate(base_url)
    expect(page).to_have_title(page_obj.title)
