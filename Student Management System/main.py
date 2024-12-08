from classes import StudentManager


def main():
    print("Welcome to Student Management System:")
    StudentManager.load_student_data(StudentManager.json_file_name)
    while True:
        print("\n1. Add Student")
        print("2. View Student Details")
        print("3. Update Student Grade")
        print("4. View All Students")
        print("5. Remove Student")
        print("6. Sort Students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            StudentManager.add_student()
        elif choice == '2':
            StudentManager.view_student_details()
        elif choice == '3':
            StudentManager.update_student_details()
        elif choice == '4':
            StudentManager.view_all_students()
        elif choice == '5':
            StudentManager.remove_student()
        elif choice == '6':
            StudentManager.sort_students()
        elif choice == '7':
            print("\nThank You For Visiting :)")
            break
        else:
            print("\nInvalid Choice. Please try again!")


if __name__ == "__main__":
    main()
