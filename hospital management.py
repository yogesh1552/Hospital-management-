class HospitalManagementSystem:
    def __init__(self, total_beds, total_doctors):
        self.total_beds = total_beds
        self.total_doctors = total_doctors
        self.occupied_beds = 0
        self.patients = []
    def admit_patient(self, patient_name):
        if self.occupied_beds < self.total_beds:
            self.patients.append(patient_name)
            self.occupied_beds += 1
            print(f"Patient {patient_name} admitted successfully.")
        else:
            print("No beds available. Cannot admit patient.")
    def discharge_patient(self, patient_name):
        if patient_name in self.patients:
            self.patients.remove(patient_name)
            self.occupied_beds -= 1
            print(f"Patient {patient_name} discharged successfully.")
        else:
            print(f"Patient {patient_name} not found.")
    def available_beds(self):
        return self.total_beds - self.occupied_beds
    def add_doctor(self, number):
        self.total_doctors += number
        print(f"{number} doctor(s) added. Total doctors: {self.total_doctors}.")

    def remove_doctor(self, number):
        if number <= self.total_doctors:
            self.total_doctors -= number
            print(f"{number} doctor(s) removed. Total doctors: {self.total_doctors}.")
        else:
            print("Not enough doctors to remove.")
    def display_status(self):
        print("\nHospital Status:")
        print(f"Total Beds: {self.total_beds}")
        print(f"Occupied Beds: {self.occupied_beds}")
        print(f"Available Beds: {self.available_beds()}")
        print(f"Total Doctors: {self.total_doctors}")
        print(f"Patients: {', '.join(self.patients) if self.patients else 'No patients currently.'}")
        print("-" * 30)
def main():
    hospital = HospitalManagementSystem(total_beds=10, total_doctors=5)
    while True:
        print("\nHospital Management System")
        print("1. Admit a Patient")
        print("2. Discharge a Patient")
        print("3. Check Available Beds")
        print("4. Add Doctors")
        print("5. Remove Doctors")
        print("6. Display Hospital Status")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            patient_name = input("Enter patient name: ")
            hospital.admit_patient(patient_name)
        elif choice == "2":
            patient_name = input("Enter patient name: ")
            hospital.discharge_patient(patient_name)
        elif choice == "3":
            print(f"Available Beds: {hospital.available_beds()}")
        elif choice == "4":
            num_doctors = int(input("Enter number of doctors to add: "))
            hospital.add_doctor(num_doctors)
        elif choice == "5":
            num_doctors = int(input("Enter number of doctors to remove: "))
            hospital.remove_doctor(num_doctors)
        elif choice == "6":
            hospital.display_status()
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
if __name__ == "__main__":
    main()
