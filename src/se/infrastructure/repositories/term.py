"""Term repository."""

import os
from typing import Any

import psycopg

from se.domain import PresentationCardProto, TermProto

from .abstract import AddRepository, ListRepository

DB_NAME = os.getenv('DATABASE_NAME', 'se')
DB_USER = os.getenv('DATABASE_USER', 'se_user')
DB_CONNINFO = f'dbname={DB_NAME} user={DB_USER}'
ALLOWED_FILTERS = {"id", "definition_id", "explanation_id"}


class TermRepository(
    AddRepository[PresentationCardProto],
    ListRepository[TermProto],
):
    def add(self, items: list[PresentationCardProto]) -> list[int]:
        if not items:
            return []

        term_ids: list[int] = []

        with psycopg.connect(DB_CONNINFO) as conn:
            with conn.cursor() as cur:
                for item in items:
                    cur.execute(
                        """
                        INSERT INTO glossary_definition (text)
                        VALUES (%s)
                        ON CONFLICT (text) DO NOTHING
                        RETURNING id
                        """,
                        (item.definition,),
                    )
                    row = cur.fetchone()
                    if row is not None:
                        def_id = row
                    else:
                        cur.execute(
                            'SELECT id FROM glossary_definition WHERE text = %s',  # noqa
                            (item.definition,),
                        )
                        def_id = cur.fetchone()  # type: ignore[assignment]

                    cur.execute(
                        """
                        INSERT INTO glossary_explanation (text)
                        VALUES (%s)
                        ON CONFLICT (text) DO NOTHING
                        RETURNING id
                        """,
                        (item.explanation,),
                    )
                    row = cur.fetchone()
                    if row is not None:
                        exp_id = row
                    else:
                        cur.execute(
                            'SELECT id FROM glossary_explanation WHERE text = %s',  # noqa
                            (item.explanation,),
                        )
                        exp_id = cur.fetchone()  # type: ignore[assignment]

                    cur.execute(
                        """
                        INSERT INTO glossary_term (definition_id, explanation_id)
                        VALUES (%s, %s)
                        ON CONFLICT (definition_id, explanation_id) DO NOTHING
                        RETURNING id
                        """,  # noqa
                        (def_id, exp_id),
                    )
                    row = cur.fetchone()
                    if row is not None:
                        term_ids.append(row)  # type: ignore[arg-type]
                    else:
                        cur.execute(
                            """
                            SELECT id FROM glossary_term
                            WHERE definition_id = %s AND explanation_id = %s
                            """,
                            (def_id, exp_id),
                        )
                        term_ids.append(cur.fetchone())  # type: ignore[arg-type]

        return term_ids

    def list(
        self,
        limit: int | None = None,
        **filters: dict[str, Any]
    ) -> list[TermProto]:
        with psycopg.connect(DB_CONNINFO) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, definition_id, explanation_id
                    FROM glossary_term
                    WHERE 
                    """
                )

class InMemoryTermRepository(
    AddRepository[TermProto],
    ListRepository[TermProto],
):
    def __init__(self) -> None:
        self._terms: set[TermProto] = set()

    # REFACTOR: Update item adding in in-memory repo
    def add(self, items: list[TermProto]) -> list[int]:
        current_ids = [term.id for term in self._terms]
        self._terms.update(items)
        updated_ids = [term.id for term in self._terms]
        return list(set(updated_ids) - set(current_ids))

    def list(
        self,
        limit: int | None = None,
        **filters: dict[str, Any],
    ) -> list[TermProto]:
        return list(self._terms)
