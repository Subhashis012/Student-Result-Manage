import json
import os

DATA_FILE = "students_data.json"

# Load existing data from file (if it exists)
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save current data to file
def save_data(student):
    with open(DATA_FILE, "w") as f:
        json.dump(student, f, indent=4)
    print("Data saved successfully!")

# Load student data at startup
student = load_data()

while True:
    print("\n------- STUDENT MANAGER APP-------")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Check Result")
    print("4. Save & Exit")
    print("5. Exit Without Saving")

    choice = input("Enter Your Choice (1-5): ")

    if choice == "1":
        name = input("Enter Student Name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks
        print(f"{name}'s marks added! (Not saved yet — choose 4 to Save & Exit)")

    # View students
    elif choice == "2":
        if not student:
            print("No Student Data Found!")
        else:
            print(f"\n{'Name':<20} {'Marks':<10} {'Result'}")
            print("-" * 40)
            for name, marks in student.items():
                result = "PASS" if marks >= 40 else "FAIL"
                print(f"{name:<20} {marks:<10} {result}")

    # Check result
    elif choice == "3":
        name = input("Enter student name to check result: ")
        if name in student:
            marks = student[name]
            result = "PASS" if marks >= 40 else "FAIL"
            print(f"Result for {name} (Marks: {marks}): {result}")
        else:
            print("Student not found!")

    # Save & Exit
    elif choice == "4":
        save_data(student)
        print("Exiting...")
        break

    # Exit without saving
    elif choice == "5":
        print("Exiting without saving...")
        break

    else:
        print("Invalid choice! Please enter a number between 1-5.")