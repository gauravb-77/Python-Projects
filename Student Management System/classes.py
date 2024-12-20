import json
from json import JSONDecodeError
from tabulate import tabulate

class Student:
    def __init__(self, name, grade):
        self.roll_number = None
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Roll No.: {self.roll_number}, Name: {self.name}, Grade: {self.grade}"


class StudentManager:
    students = []
    json_file_name = "students_data.json"
    table_style = "grid"

    @classmethod
    def _modify_roll_numbers(cls): # Marked as "private" for internal use
        for index, student in enumerate(cls.student_obj_list):
            student["Roll No."] = index+1

    @classmethod
    def get_valid_input_roll_number(cls, prompt):
        while True:
            roll_number_input = input(prompt)
            if not roll_number_input.isdigit():
                print("Roll number must be positive integer. Please try again.")
                continue
            elif roll_number_input == '0':
                print("Roll number cannot be zero. Please try again.")
                continue
            elif int(roll_number_input) not in range(1, len(cls.student_obj_list) + 1):
                print(f"Student with roll number {roll_number_input} does not exist. Please try again.")
                continue

            return int(roll_number_input)

    @staticmethod
    def get_valid_input_grade(prompt):
        while True:
            grade_input = input(prompt)
            if not grade_input or grade_input.lower() not in 'abcdef':
                print("\nInvalid Grade. Please try again.")
                continue

            return grade_input.upper()

    @staticmethod
    def get_valid_input_name(prompt):
        while True:
            name_input = input(prompt).strip()
            if len(name_input) > 50 or len(name_input) < 2:
                print("Name must be between 2 and 50 characters. Please try again.")
                continue
            if not name_input[0].isalpha():
                print("\nInvalid name. Please try again.")
                continue
            for char in name_input:
                if not char.isalpha() and char not in ['-', "'", ' ']:
                    print("\nInvalid name. Please try again.")
                    break
            else:
                return name_input

    @classmethod
    def load_student_data(cls, file):
        try:
            with open(file, 'r') as student_json_data_file:
                cls.student_obj_list = json.load(student_json_data_file)
        except FileNotFoundError:
            cls.student_obj_list = []
        except JSONDecodeError:
            print("JSON data is invalid")

    @classmethod
    def _save_student_data(cls, file):
        student_json_objects_list = json.dumps(cls.student_obj_list, indent=4)

        with open(file, 'w') as data_file:
            data_file.write(student_json_objects_list)


    @classmethod
    def add_student(cls):
        name_input_prompt = "\nEnter student's name: "
        name_input = cls.get_valid_input_name(name_input_prompt)

        grade_input_prompt = "Enter student's grade (91-100 = A, 81-90 = B, 71-80 = C, 61-70 = D, 51-60 = E, Fail = F): "
        grade_input = cls.get_valid_input_grade(grade_input_prompt)

        new_student = Student(name_input, grade_input)

        new_student_obj = {
            "Roll No.": len(cls.student_obj_list)+1,
            "Name": new_student.name,
            "Grade": new_student.grade
        }

        cls.student_obj_list.append(new_student_obj)

        cls._save_student_data(cls.json_file_name)
        print("Student added successfully!")

        cls.view_all_students()

    @classmethod
    def remove_student(cls):
        if not cls.student_obj_list:
            print("\nNo students available to remove. Add students first.")
            return

        roll_number_input_prompt = "\nEnter student's roll number who you want to remove: "
        roll_number_input = cls.get_valid_input_roll_number(roll_number_input_prompt)

        targeted_student = cls.student_obj_list[roll_number_input-1]
        targeted_student_name = targeted_student["Name"]

        while True:
            confirm_remove = input(f"Are you sure you want to remove '{targeted_student_name}'? [Y/N]: ")
            if confirm_remove.lower() == 'y':
                cls.student_obj_list.remove(targeted_student)
                cls._modify_roll_numbers() # Called automatically after removal
                cls._save_student_data(cls.json_file_name)
                print(f"\n'{targeted_student_name}' has been removed successfully.")

                cls.view_all_students()
                break
            elif confirm_remove.lower() == 'n':
                break
            else:
                print("Invalid input. Please try again.")

    @classmethod
    def update_student_details(cls):
        if not cls.student_obj_list:
            print("\nNo students available to update details. Add students first.")
            return

        roll_number_input_prompt = "\nEnter student's roll number whose details you want to update: "
        roll_number_input = cls.get_valid_input_roll_number(roll_number_input_prompt)

        while True:
            update_attribute = input("\nEnter 1 to update name, 2 to update grade: ")
            if update_attribute == '1':
                name_input_prompt = "\nEnter updated name of the student: "
                name_input = cls.get_valid_input_name(name_input_prompt)

                for student in cls.student_obj_list:
                    if student["Roll No."] == roll_number_input:

                        if student["Name"] == name_input:
                            print("\nThe new name is the same as the current grade. No update needed.")
                        else:
                            student["Name"] = name_input
                            cls._save_student_data(cls.json_file_name)

                            print("\nUpdated student details:\n")
                            cls.display_students_data([cls.student_obj_list[roll_number_input-1]])
                        break
                break
            elif update_attribute == '2':
                grade_input_prompt = "\nEnter updated grade (91-100 = A, 81-90 = B, 71-80 = C, 61-70 = D, 51-60 = E, Fail = F): "
                grade_input = cls.get_valid_input_grade(grade_input_prompt)

                for student in cls.student_obj_list:
                    if student["Roll No."] == roll_number_input:

                        if student["Grade"] == grade_input:
                            print("\nThe new grade is the same as the current grade. No update needed.")
                        else:
                            student["Grade"] = grade_input
                            cls._save_student_data(cls.json_file_name)
                        break
                break
            else:
                print("\nInvalid Input. Please try again.")

    @classmethod
    def display_students_data(cls, students_data):
        headers = students_data[0].keys()
        rows = [student.values() for student in students_data]

        print(tabulate(rows, headers, tablefmt=cls.table_style))

    @classmethod
    def change_table_format(cls):
        available_styles = {
            '1': "plain",
            '2': "grid",
            '3': "fancy_grid",
            '4': "pipe",
            '5': "simple"
        }

        while True:
            print(f"\nCurrent table format: {cls.table_style}")
            print("How would you like the data to be displayed (or press Enter to keep the current)?")
            print("1. Plain")
            print("2. Grid")
            print("3. Fancy Grid")
            print("4. Pipe")
            print("5. Simple")

            table_format_choice = input("Enter your choice (1-5): ")

            if not table_format_choice:
                break
            if table_format_choice not in available_styles:
                print("\nInvalid choice. Please try again.")
                continue

            print(f"Your desired table format '{available_styles[table_format_choice]}' is set.")
            cls.table_style =  available_styles[table_format_choice]

            break

    @classmethod
    def view_all_students(cls):
        if not cls.student_obj_list:
            print("\nNo students available to view. Add students first.")
            return
        elif len(cls.student_obj_list) == 1:
            print(f"\nWe have only {len(cls.student_obj_list)} student in our system:\n")
        else:
            print(f"\nWe have {len(cls.student_obj_list)} students in our system:\n")

        cls.display_students_data(cls.student_obj_list)

        print("Would you like to view details of a specific student?")
        while True:
            choice = input("Enter their Roll Number (or press Enter to return to the main menu): ")

            if not choice:
                break
            else:
                if not choice.isdigit():
                    print("\nRoll number must be positive integer. Please try again.")
                    continue
                elif choice == '0':
                    print("\nRoll number cannot be zero. Please try again.")
                    continue
                elif int(choice) not in range(1, len(cls.student_obj_list) + 1):
                    print(f"\nStudent with roll number {choice} does not exist. Please try again.")
                    continue

                roll_num = int(choice)
                targeted_student = cls.student_obj_list[roll_num - 1]

                print("\nHere is the student's details:")

                cls.display_students_data([targeted_student])

                break

    @classmethod
    def sort_students(cls):
        if not cls.student_obj_list:
            print("\nNo students available to sort. Add students first.")
            return

        while True:
            print("\nChoose sorting criteria:")
            print("1. Roll Number")
            print("2. Name")
            print("3. Grade")
            print("4. Go Back to Main Menu")
            sort_choice = input("Enter your choice (1-4): ")

            if sort_choice == '1':
                sorted_by_roll_number_data = sorted(cls.student_obj_list, key=lambda x: x["Roll No."])
                print("\nStudents sorted by Roll Number:")
                cls.display_students_data(sorted_by_roll_number_data)
            elif sort_choice == '2':
                sorted_by_name_data = sorted(cls.student_obj_list, key=lambda x: x["Name"].lower())
                print("\nStudents sorted by Name:")
                cls.display_students_data(sorted_by_name_data)
            elif sort_choice == '3':
                sorted_by_grade_data = sorted(cls.student_obj_list, key=lambda x: x["Grade"])
                print("\nStudents sorted by Grade:")
                cls.display_students_data(sorted_by_grade_data)
            elif sort_choice == '4':
                print("\nReturning to main menu.")
                break
            else:
                print("\nInvalid Choice. Please try again.")

    @classmethod
    def view_students_by_grade(cls):
        if not cls.student_obj_list:
            print("\nNo students available to view. Add students first.")
            return

        grade_input_prompt = "\nSpecify the grade you want to filter by (A, B, C, D, E, F): "
        grade_input = cls.get_valid_input_grade(grade_input_prompt)

        target_data = [student for student in cls.student_obj_list if student["Grade"] == grade_input]

        if not target_data:
            print(f"No students found with grade {grade_input}.")
            return

        print(f"\nAll {len(target_data)} students with grade {grade_input}:\n")

        cls.display_students_data(target_data)

    @classmethod
    def manage_data(cls):
        while True:
            print("\nData Management Options:")
            print("1. Import Students from JSON File")
            print("2. Export Students to JSON File")
            print("3. Back to Main Menu")

            choice = input("\nEnter your choice (1-3): ")

            if choice not in '123':
                print("Invalid choice. Please try again.")
                continue

            if choice == '2':
                pass


