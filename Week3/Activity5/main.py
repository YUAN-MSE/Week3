from pathlib import Path

from app.config import load_config
from app.db_client import DatabaseClient, DatabaseConfig
from app.logger import setup_logging
from app.reporting import print_patients


def main() -> None:
    config_path = Path(__file__).resolve().parent / "config.yaml"
    config = load_config(config_path)
    logger = setup_logging(config.logging.level)

    if not config.db.path.exists():
        logger.error("database not found at %s", config.db.path)
        logger.error("run: python db_setup.py")
        return

    db_client = DatabaseClient(
        DatabaseConfig(
            path=config.db.path,
            enforce_foreign_keys=config.db.enforce_foreign_keys,
        )
    )

    logger.info("querying senior patients (age >= %s)", config.queries.senior_age)
    seniors = db_client.get_senior_patients(config.queries.senior_age)
    print_patients("Senior Patients:", seniors)

    logger.info("counting doctors (%s)", config.queries.specialisation)
    total = db_client.count_doctors_by_specialisation(config.queries.specialisation)
    print(f"\nTotal {config.queries.specialisation} Doctors: {total}")


if __name__ == "__main__":
    main()
