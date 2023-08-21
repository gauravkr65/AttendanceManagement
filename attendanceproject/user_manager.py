# user_manager.py
import session_manager
from student_manager import student_database

user_database = {
    "gaurav": "pass",
    "username2": "password2",
}

def login_user():
    global session_manager
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in user_database and user_database[username] == password:
        print("Login successful.")
        session_manager.current_user = username
        return True
    else:
        print("Invalid credentials.")
        return False

#  Student login function
def student_login():
    student_id = input("Enter your student ID: ")
    if student_id in student_database:
        student_info = student_database[student_id]
        print("Attendance Records for", student_info["name"])
        attendance_data = student_info.get("attendance", {})
        for date, status in attendance_data.items():
            print(date, ":", status)
    else:
        print("Student not found.")     