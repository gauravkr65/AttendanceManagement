# student_manager.py
import session_manager

# Student database
student_database = {}

# Student functions
def add_student():
    if session_manager.current_user:
        num_students = int(input("Enter the number of students to add: "))
        
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            branch = input("Enter your branch: ")
            course = input("Enter your course: ")
            
            if student_id not in student_database:
                student_database[student_id] = {"name": name, "branch": branch, "course": course, "attendance": {}}
                print(f"Student {student_id} added successfully.")
            else:
                print(f"Student {student_id} already exists.")
    else:
        print("Please log in to perform this action.")


def view_student():
    if session_manager.current_user:
        student_id = input("Enter student ID: ")
        if student_id in student_database:
            student_info = student_database[student_id]
            print("Name:", student_info["name"])
            print("branch:", student_info["branch"])
            print("course:", student_info["course"])
        else:
            print("Student not found.")
    else:
        print("Please log in to perform this action.")

def update_student():
    if session_manager.current_user:
        student_id = input("Enter student ID: ")
        if student_id in student_database:
            student_info = student_database[student_id]
            field = input("Enter field to update (name/branch/course): ")
            new_value = input(f"Enter new {field}: ")
            if field in student_info:
                student_info[field] = new_value
                print("Update successful.")
            else:
                print("Invalid field.")
        else:
            print("Student not found.")
    else:
        print("Please log in to perform this action.")

def delete_student():
    if session_manager.current_user:
        student_id = input("Enter student ID: ")
        if student_id in student_database:
            del student_database[student_id]
            print("Student deleted.")
        else:
            print("Student not found.")
    else:
        print("Please log in to perform this action.")

def mark_attendance():
    if session_manager.current_user:
        mark_student = int(input("Enter number of students to mark: "))
        
        for _ in range(mark_student):
            student_id = input("Enter student ID: ")
            if student_id in student_database:
                date = input("Enter date (YYYY-MM-DD): ")
                status = input("Enter attendance status (Present/Absent): ")
                student_info = student_database[student_id]
                if date in student_info["attendance"]:
                    print("Attendance already marked for this date.")
                else:
                    student_info["attendance"][date] = status
                    print("Attendance marked.")
            else:
                print("Student not found.")
    else:
        print("Please log in to perform this action.")

def view_attendance(student_id, start_date=None, end_date=None):
    if student_id in student_database:
        student_info = student_database[student_id]
        attendance_data = student_info.get("attendance", {})
        
        if start_date and end_date:
            filtered_data = {
                date: status for date, status in attendance_data.items()
                if start_date <= date <= end_date
            }
        else:
            filtered_data = attendance_data

        print("Attendance Records for", student_info["name"])
        for date, status in filtered_data.items():
            print(date, ":", status)
    else:
        print("Student not found.")
        
def get_attendance_data(student_id):
    if student_id in student_database:
        student_info = student_database[student_id]
        attendance_data = student_info.get("attendance", {})
        return attendance_data
    else:
        print("Student not found.")
        return {}

# Student information menu
def student_info_menu():
    while True:
        print("\nStudent Information Menu:")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back to User Menu")

        student_info_choice = input("Enter your choice: ")

        if student_info_choice == "1":
            add_student()
        elif student_info_choice == "2":
            view_student()
        elif student_info_choice == "3":
            update_student()
        elif student_info_choice == "4":
            delete_student()
        elif student_info_choice == "5":
            break
        else:
            print("Invalid choice. Please choose again.")