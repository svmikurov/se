"""Term repository tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

from se.domain import Term

if TYPE_CHECKING:
    from typing import Any

    from .types import RepoProto


def test_repo_returns_term_object_list(
    terms_data: list[dict[str, Any]],
    in_memory_term_repo: RepoProto,
) -> None:
    expected = [Term(**term) for term in terms_data]
    in_memory_term_repo.add(expected)

    terms = in_memory_term_repo.list()

    assert len(terms) == len(expected)
    assert set(terms) == set(expected)
