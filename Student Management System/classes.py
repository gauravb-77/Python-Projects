import json

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


    @classmethod
    def _modify_roll_numbers(cls): # Marked as "private" for internal use
        for index, student in enumerate(cls.student_obj_list):
            student["Roll No."] = index+1

    @classmethod
    def get_valid_input_roll_number(cls, prompt):
        while True:
            roll_number_input = input(prompt)
            if not roll_number_input.isdigit():
                print("Roll number must be positive integer. Please try again :(")
                continue
            elif roll_number_input == '0':
                print("Roll number cannot be zero. Please try again :(")
                continue
            elif int(roll_number_input) not in range(1, len(cls.student_obj_list) + 1):
                print(f"Student with roll number {roll_number_input} does not exist. Please try again :(")
                continue

            return int(roll_number_input)

    @staticmethod
    def get_valid_input_grade(prompt):
        while True:
            grade_input = input(prompt)
            if not grade_input.lower() in 'abcdef':
                print("\nInvalid Grade. Please try again.")
                continue

            return grade_input.upper()

    @classmethod
    def load_student_data(cls, file):
        try:
            with open(file, 'r') as student_json_data_file:
                cls.student_obj_list = json.load(student_json_data_file)
        except FileNotFoundError:
            cls.student_obj_list = []

    @classmethod
    def _save_student_data(cls, file):
        student_json_objects_list = json.dumps(cls.student_obj_list, indent=4)

        with open(file, 'w') as data_file:
            data_file.write(student_json_objects_list)


    @classmethod
    def add_student(cls):
        name = input("Enter student's name: ")

        grade_input_prompt = "Enter student's grade (91-100 = A, 81-90 = B, 71-80 = C, 61-70 = D, 51-60 = E, Fail = F): "
        grade_input = cls.get_valid_input_grade(grade_input_prompt)

        new_student = Student(name, grade_input)

        new_student_obj = {
            "Roll No.": len(cls.student_obj_list)+1,
            "Name": new_student.name,
            "Grade": new_student.grade
        }

        cls.student_obj_list.append(new_student_obj)

        cls._save_student_data(cls.json_file_name)
        print("Student added successfully!\n")

        cls.view_all_students()

    @classmethod
    def remove_student(cls):
        if not cls.student_obj_list:
            print("\nNo students available to remove. Add students first.")
            return

        roll_number_input_prompt = "\nEnter student's roll number who you want to remove: "
        roll_number_input = cls.get_valid_input_roll_number(roll_number_input_prompt)

        for student in cls.student_obj_list:
            if student["Roll No."] == roll_number_input:
                cls.student_obj_list.remove(student)
                cls._modify_roll_numbers() # Called automatically after removal
                cls._save_student_data(cls.json_file_name)
                print(f"\n{student["Name"]} has been removed successfully.")
                break

        cls.view_all_students()

    @classmethod
    def view_student_details(cls):
        if not cls.student_obj_list:
            print("\nCurrently there is no any student present in our list. First add students.")
            return

        prompt = "\nEnter student's roll number whose details you want to see: "
        roll_number_input = cls.get_valid_input_roll_number(prompt)

        for student in cls.student_obj_list:
            if student["Roll No."] == roll_number_input:
                print("\nHere is the student's details:")
                print(f"Roll No.: {student["Roll No."]}, Name: {student["Name"]}, Grade: {student["Grade"]}")
                break

    @classmethod
    def update_student_details(cls):
        if not cls.student_obj_list:
            print("\nCurrently there is no any student present in our list. First add students.")
            return

        roll_number_input_prompt = "\nEnter student's roll number whose details you want to update: "
        roll_number_input = cls.get_valid_input_roll_number(roll_number_input_prompt)

        while True:
            update_attribute = input("Enter 1 to update name, 2 to update grade: ")
            if update_attribute == '1':
                name_input = input("\nEnter updated name of the student: ")

                for student in cls.student_obj_list:
                    if student["Roll No."] == roll_number_input:

                        if student["Name"] == name_input:
                            print("\nThe new name is the same as the current grade. No update needed.")
                        else:
                            student["Name"] = name_input
                            cls._save_student_data(cls.json_file_name)
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
                print("Invalid Input. Try again :)")

    @classmethod
    def view_all_students(cls):
        if not cls.student_obj_list:
            print("\nCurrently there is no any student present in our list. First add students.")
            return

        print("\nThese are all our students:\n")
        for student in cls.student_obj_list:
            print(f"{student["Roll No."]}. {student["Name"]}")

