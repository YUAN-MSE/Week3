# Clinic Management System (Week 3)

## What this is
This is a small SQLite clinic system for Week 3. It has three tables (clinic, patient, doctor) and two simple reports:
- list senior patients
- count ophthalmology doctors

## How it works
- `db_setup.py` resets and seeds the database
- `main.py` runs the queries and prints results
- `config.yaml` stores the DB path and query settings

## Run
```
python db_setup.py
python main.py
```

## Project files
- `app/` - config, logging, data access, reporting
- `db/` - schema and seed data
- `config.yaml`
- `ER_Diagram.md`

## Example output
```
Senior Patients:
John Smith | Age 70 | Male | 021111111 | Auckland
Maria Green | Age 72 | Female | 021444444 | Wellington

Total Ophthalmology Doctors: 2
```

## Notes
If you change the schema or seed data, run `db_setup.py` again.
