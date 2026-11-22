"""Term repository."""

import os
from typing import Any

import psycopg

from se.domain import PresentationCardProto, TermProto

from .abstract import AddRepository, ListRepository

DB_NAME = os.getenv('DATABASE_NAME', 'se')
DB_USER = os.getenv('DATABASE_USER', 'se_user')


class TermRepository(
    AddRepository[PresentationCardProto],
    ListRepository[TermProto],
):

    def add(self, items: list[PresentationCardProto]) -> list[int]:
        if not items:
            return []

        term_ids: list[int] = []

        with psycopg.connect(f"dbname={DB_NAME} user={DB_USER}") as conn:
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
                            "SELECT id FROM glossary_definition WHERE text = %s",
                            (item.definition,),
                        )
                        def_id = cur.fetchone()

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
                            "SELECT id FROM glossary_explanation WHERE text = %s",
                            (item.explanation,),
                        )
                        exp_id = cur.fetchone()

                    cur.execute(
                        """
                        INSERT INTO glossary_term (definition_id, explanation_id)
                        VALUES (%s, %s)
                        ON CONFLICT (definition_id, explanation_id) DO NOTHING
                        RETURNING id
                        """,
                        (def_id, exp_id),
                    )
                    row = cur.fetchone()
                    if row is not None:
                        term_ids.append(row)
                    else:
                        cur.execute(
                            """
                            SELECT id FROM glossary_term
                            WHERE definition_id = %s AND explanation_id = %s
                            """,
                            (def_id, exp_id),
                        )
                        term_ids.append(cur.fetchone())

        return term_ids



class InMemoryTermRepository(
    AddRepository[TermProto],
    ListRepository[TermProto],
):
    def __init__(self) -> None:
        self._terms: set[TermProto] = set()

    def add(self, items: list[TermProto]) -> None:
        self._terms.update(items)

    def list(
        self,
        limit: int | None = None,
        **filters: dict[str, Any],
    ) -> list[TermProto]:
        return list(self._terms)
