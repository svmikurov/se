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


class PresentationPage(BasePage):
    path = '/glossary/presentation/'
    title = 'Презентация'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._set_locators()

    def _set_locators(self) -> None:
        self.question_text = self.page.get_by_test_id('question-text')
        self.answer_text = self.page.get_by_test_id('answer-text')


@pytest.mark.e2e
class TestGlossaryAppPage:
    def test_index_has_title(self, page: Page, base_url: str) -> None:
        page_obj = GlossaryPage(page)
        page_obj.navigate(base_url)
        expect(page).to_have_title(page_obj.title)


@pytest.mark.e2e
class TestGlossaryPresentationPage:
    def test_page_has_title(self, page: Page, base_url: str) -> None:
        page_obj = PresentationPage(page)
        page_obj.navigate(base_url)
        expect(page).to_have_title(page_obj.title)

    def test_page_shows_definition(self, page: Page, base_url: str) -> None:
        page_obj = PresentationPage(page)
        page_obj.navigate(base_url)
        expect(page_obj.question_text).to_be_visible()
        expect(page_obj.answer_text).to_be_visible()
