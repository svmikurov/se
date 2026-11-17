"""Request handler tests."""

from se.entrypoints.web.handlers import RequestHandler


def test_handler_returns_card() -> None:
    handler = RequestHandler()
    card = handler.handle()

    assert card.definition == 'Definition text'
    assert card.explanation == 'Explanation text'
