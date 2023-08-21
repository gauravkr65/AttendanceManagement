# main.py
import session_manager
import user_manager
import student_manager
import report_manager

# Main loop
while True:
    print("\nMain Menu:")
    print("1. User Login")
    print("2. Student Login")
    print("3. Exit")

    main_choice = input("Enter your choice: ")

    if main_choice == "1":
        user_manager.login_user()
        if session_manager.current_user:
            while True:
                print("\nUser Menu:")
                print("1. Student Information")
                print("2. Mark Attendance")
                print("3. View Attendance")
                print("4. Generate Report")
                print("5. Generate CSV File")
                print("6. Logout")

                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    student_manager.student_info_menu()
                elif user_choice == "2":
                    student_manager.mark_attendance()
                elif user_choice == "3":
                    student_id = input("Enter student id: ")
                    student_manager.view_attendance(student_id)
                elif user_choice == "4":
                    report_manager.generate_report_menu()
                elif user_choice == "5":
                    if session_manager.current_user:
                        csv_filename = "all_students_attendance.csv"
                        report_manager.generate_csv_file(csv_filename, student_manager.student_database)
                    else:
                        print("You need to be logged in.")
                elif user_choice == "6":
                    print("Logging out.")
                    session_manager.current_user = None
                    break
                else:
                    print("Invalid choice. Please choose again.")
    elif main_choice == "2":
        user_manager.student_login()
    elif main_choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose again.")
