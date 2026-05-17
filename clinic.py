# clinic.py — Patient Management System v1.0

patients = []

def add_patient(name, age):
    patient = {"name": name, "age": age}
    patients.append(patient)
    print("Patient added.")

def view_patients():
    for p in patients:
        print(p)

def main():
    add_patient("Nimal", 35)
    add_patient("Amali", 28)
    view_patients()

main()