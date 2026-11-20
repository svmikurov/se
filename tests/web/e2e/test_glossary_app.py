from urllib.parse import urljoin

import pytest
from playwright.sync_api import Page, Response, expect

pytestmark = pytest.mark.e2e


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


class PresentationPage(BasePage):
    path = '/glossary/presentation/'
    title = 'Презентация'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._set_locators()

    def _set_locators(self) -> None:
        self.question_locator = self.page.get_by_test_id('question-text')
        self.answer_locator = self.page.get_by_test_id('answer-text')


class TestGlossaryIndexPage:
    def test_has_title(self, page: Page, base_url: str) -> None:
        page_obj = GlossaryPage(page)
        page_obj.navigate(base_url)
        expect(page).to_have_title(page_obj.title)


class TestGlossaryPresentationPage:
    def test_has_title(self, page: Page, base_url: str) -> None:
        page_obj = PresentationPage(page)
        page_obj.navigate(base_url)
        expect(page).to_have_title(page_obj.title)

    def test_shows_card(self, page: Page, base_url: str) -> None:
        page_obj = PresentationPage(page)
        page_obj.navigate(base_url)
        expect(page_obj.question_locator).to_have_text('Definition text')
        expect(page_obj.answer_locator).to_have_text('Explanation text')
