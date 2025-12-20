from dataclasses import dataclass


@dataclass(frozen=True)
class Patient:
    patient_id: int
    full_name: str
    age: int
    gender: str
    phone: str
    address: str
    clinic_id: int


@dataclass(frozen=True)
class Doctor:
    doctor_id: int
    full_name: str
    specialisation: str
    clinic_id: int
