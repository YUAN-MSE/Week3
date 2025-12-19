import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

from app.models import Doctor, Patient


@dataclass(frozen=True)
class DatabaseConfig:
    path: Path
    enforce_foreign_keys: bool


class DatabaseClient:
    def __init__(self, config: DatabaseConfig):
        self.config = config

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.config.path)
        conn.row_factory = sqlite3.Row
        if self.config.enforce_foreign_keys:
            conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def get_senior_patients(self, min_age: int) -> List[Patient]:
        query = """
            SELECT patient_id, full_name, age, gender, phone, address, clinic_id
            FROM patient
            WHERE age >= ?
            ORDER BY age DESC, full_name
        """
        with self._connect() as conn:
            rows = conn.execute(query, (min_age,)).fetchall()
        return [Patient(**dict(row)) for row in rows]

    def count_doctors_by_specialisation(self, specialisation: str) -> int:
        query = "SELECT COUNT(*) AS total FROM doctor WHERE specialisation = ?"
        with self._connect() as conn:
            row = conn.execute(query, (specialisation,)).fetchone()
        return int(row[0])

    def apply_schema(self, schema_sql: str) -> None:
        with self._connect() as conn:
            conn.executescript(schema_sql)

    def seed_table(self, statement: str, rows: Iterable[tuple]) -> None:
        with self._connect() as conn:
            conn.executemany(statement, rows)
