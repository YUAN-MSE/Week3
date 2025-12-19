from typing import Iterable

from app.models import Patient


def print_patients(title: str, patients: Iterable[Patient]) -> None:
    print(title)
    printed = False
    for patient in patients:
        printed = True
        print(
            f"{patient.full_name} | Age {patient.age} | {patient.gender} | "
            f"{patient.phone} | {patient.address}"
        )
    if not printed:
        print("- none -")
