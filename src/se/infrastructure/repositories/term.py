"""Term repository."""

import os

import psycopg

from se.domain import Displayed

from .abstract import AddRepository

DB_NAME = os.getenv('DATABASE_NAME', 'se')
DB_USER = os.getenv('DATABASE_USER', 'se_user')
DB_CONNINFO = f'dbname={DB_NAME} user={DB_USER}'
ALLOWED_FILTERS = {'id', 'definition_id', 'explanation_id'}


class TermRepository(
    AddRepository[Displayed],
):
    def add(self, items: list[Displayed]) -> list[int]:
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
                        (item.meaning,),
                    )
                    row = cur.fetchone()
                    if row is not None:
                        exp_id = row
                    else:
                        cur.execute(
                            'SELECT id FROM glossary_explanation WHERE text = %s',  # noqa
                            (item.meaning,),
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
