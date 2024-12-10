from classes import StudentManager


def main():
    print("Welcome to the Student Management System!")
    StudentManager.load_student_data(StudentManager.json_file_name)
    while True:
        print("\n1. View All Students")
        print("2. Sort Students")
        print("3. View Students by Grade")
        print("4. Change Table Format")
        print("5. Add Student")
        print("6. Update Student Details")
        print("7. Remove Student")
        print("8. Data Management")
        print("9. Exit\n")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            StudentManager.view_all_students()
        elif choice == '2':
            StudentManager.sort_students()
        elif choice == '3':
            StudentManager.view_students_by_grade()
        elif choice == '4':
            StudentManager.change_table_format()
        elif choice == '5':
            StudentManager.add_student()
        elif choice == '6':
            StudentManager.update_student_details()
        elif choice == '7':
            StudentManager.remove_student()
        elif choice == '8':
            StudentManager.manage_data()
        elif choice == '9':
            print("\nThank You For Visiting :)")
            break
        else:
            print("\nInvalid Choice. Please try again!")


if __name__ == "__main__":
    main()
