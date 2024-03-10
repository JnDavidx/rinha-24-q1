import os
from typing import Any

from psycopg_pool import ConnectionPool


class CrebitoDB:

    __slots__ = ["_pool"]

    def __init__(self) -> None:
        self._pool = ConnectionPool(
            os.getenv("PG_CONNECTION_STRING"),
            max_size=6,
            kwargs={"prepare_threshold": 0}
        )
        self._pool.wait()

    def insert_transaction(
        self, id_: int, value: int, type_: str, description: str
    ) -> dict[str, int] | bool | None:
        with self._pool.connection() as conn:
            [client] = conn.execute(
                "SELECT make_transaction (%s, %s, %s, %s)",
                [id_, value, type_, description]
            ).fetchone()

            return client

    def get_statement(self, id_: int) -> dict[str, Any] | None:
        with self._pool.connection() as conn:
            [statement] = conn.execute(
                "SELECT get_statement (%s)", [id_]
            ).fetchone()

            if statement and statement["ultimas_transacoes"] is None:
                statement["ultimas_transacoes"] = []

            return statement
