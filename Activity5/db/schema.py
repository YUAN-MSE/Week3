SCHEMA_SQL = """
DROP TABLE IF EXISTS patient;
DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS clinic;

CREATE TABLE clinic (
    clinic_id INTEGER PRIMARY KEY,
    clinic_name TEXT NOT NULL,
    location TEXT NOT NULL,
    phone TEXT NOT NULL
);

CREATE TABLE patient (
    patient_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    clinic_id INTEGER NOT NULL,
    FOREIGN KEY (clinic_id) REFERENCES clinic(clinic_id)
);

CREATE TABLE doctor (
    doctor_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    specialisation TEXT NOT NULL,
    clinic_id INTEGER NOT NULL,
    FOREIGN KEY (clinic_id) REFERENCES clinic(clinic_id)
);
"""
