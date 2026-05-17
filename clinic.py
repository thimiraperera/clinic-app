# clinic.py — Patient Management System v1.0

patients = []

def add_patient(name, age, condition, doctor):
 patient = {
 "name": name,
 "age": age,
 "condition": condition,
 "doctor": doctor
 }
 patients.append(patient)
 print(f"Patient {name} added under Dr. {doctor}.")

def view_patients():
    for p in patients:
        print(p)

def main():
 add_patient("Nimal", 35, "Diabetes", "Dr. Silva")
 add_patient("Amali", 28, "Hypertension", "Dr. Perera")
 view_patients()

main()