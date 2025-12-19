from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

import yaml


@dataclass(frozen=True)
class DBConfig:
    path: Path
    enforce_foreign_keys: bool


@dataclass(frozen=True)
class QueryConfig:
    senior_age: int
    specialisation: str


@dataclass(frozen=True)
class LogConfig:
    level: str


@dataclass(frozen=True)
class AppConfig:
    db: DBConfig
    queries: QueryConfig
    logging: LogConfig


def _resolve_path(raw_path: str, base_dir: Path) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    return (base_dir / path).resolve()


def load_config(config_path: Path) -> AppConfig:
    if not config_path.exists():
        raise FileNotFoundError(f"Missing config file: {config_path}")

    raw: Dict[str, Any]
    with config_path.open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}

    base_dir = config_path.parent
    db_raw = raw.get("database", {})
    query_raw = raw.get("queries", {})
    log_raw = raw.get("logging", {})

    db_config = DBConfig(
        path=_resolve_path(db_raw.get("path", "clinic.db"), base_dir),
        enforce_foreign_keys=bool(db_raw.get("enforce_foreign_keys", True)),
    )
    query_config = QueryConfig(
        senior_age=int(query_raw.get("senior_age", 65)),
        specialisation=str(query_raw.get("specialisation", "Ophthalmology")),
    )
    log_config = LogConfig(level=str(log_raw.get("level", "INFO")))

    return AppConfig(db=db_config, queries=query_config, logging=log_config)
