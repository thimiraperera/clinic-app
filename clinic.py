# clinic.py — Patient Management System v1.0

patients = []

def add_patient(name, age):
 patient_id = len(patients) + 1
 patient = {
 "id": patient_id,
 "name": name,
 "age": age
 }
 patients.append(patient)
 print(f"Patient {name} added with ID: {patient_id}.")

def view_patients():
    for p in patients:
        print(p)

def search_patient(name):
    results = [p for p in patients if p["name"].lower() == name.lower()]
    if results:
        print("Found:", results)
    else:
        print(f"No patient found with name: {name}")

def main():
    add_patient("Nimal", 35)
    add_patient("Amali", 28)
    view_patients()
    search_patient("Nimal")
    search_patient("Kamal")

main()