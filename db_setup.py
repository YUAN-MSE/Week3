from pathlib import Path

from app.config import load_config
from app.db_client import DatabaseClient, DatabaseConfig
from app.logger import setup_logging
from db.schema import SCHEMA_SQL
from db.seed import CLINICS, DOCTORS, PATIENTS


def main() -> None:
    config_path = Path(__file__).resolve().parent / "config.yaml"
    config = load_config(config_path)
    logger = setup_logging(config.logging.level)

    db_client = DatabaseClient(
        DatabaseConfig(
            path=config.db.path,
            enforce_foreign_keys=config.db.enforce_foreign_keys,
        )
    )

    logger.info("resetting database at %s", config.db.path)
    db_client.apply_schema(SCHEMA_SQL)

    logger.info("seeding clinics")
    db_client.seed_table(
        "INSERT INTO clinic (clinic_id, clinic_name, location, phone) VALUES (?, ?, ?, ?)",
        CLINICS,
    )

    logger.info("seeding patients")
    db_client.seed_table(
        """
        INSERT INTO patient (patient_id, full_name, age, gender, phone, address, clinic_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        PATIENTS,
    )

    logger.info("seeding doctors")
    db_client.seed_table(
        """
        INSERT INTO doctor (doctor_id, full_name, specialisation, clinic_id)
        VALUES (?, ?, ?, ?)
        """,
        DOCTORS,
    )

    logger.info("database setup completed")


if __name__ == "__main__":
    main()
