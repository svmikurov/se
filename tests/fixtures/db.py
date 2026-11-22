"""Database connection pytest fixtures."""

import os

import psycopg
import pytest
from psycopg.rows import dict_row


def get_db_password() -> str:
    secret_path = os.environ.get('DATABASE_PASSWORD_FILE')
    if secret_path and os.path.exists(secret_path):
        with open(secret_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    return os.environ.get('DATABASE_PASSWORD', '')


@pytest.fixture(scope='session')
def db_conn():  # type: ignore[no-untyped-def]
    """Одно подключение к тестовой БД на всю сессию тестов."""
    conn = psycopg.connect(
        host=os.environ['DATABASE_HOST'],
        dbname=os.environ['DATABASE_NAME'],
        user=os.environ['DATABASE_USER'],
        password=get_db_password(),
        row_factory=dict_row,
        autocommit=True,
    )
    yield conn
    conn.close()


@pytest.fixture
def create_definition(db_conn):  # type: ignore[no-untyped-def]
    created_ids = []

    def _insert(user_id: int, definition: str):  # type: ignore[no-untyped-def]
        with db_conn.cursor() as cur:
            cur.execute(
                """
                """,
                (user_id, definition),
            )
            row = cur.fetchone()
            created_ids.append(row['id'])
            return row

    yield _insert

    # Clean
    if created_ids:
        with db_conn.cursor() as cur:
            cur.execute(
                'DELETE FROM {{{{yourapp_item}}}} WHERE id = ANY(%s)',
                (created_ids,),
            )
