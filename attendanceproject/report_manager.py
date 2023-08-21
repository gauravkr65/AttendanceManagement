# report_manager.py
import student_manager
import csv

def generate_csv_file(filename, student_data):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Student ID", "Name", "Course", "Branch", "Date", "Status"])
        
        for student_id, student_info in student_data.items():
            name = student_info.get("name", "Unknown")
            course = student_info.get("course", "Unknown")
            branch = student_info.get("branch", "Unknown")
            attendance_data = student_info.get("attendance", {})
            
            for date, status in attendance_data.items():
                csv_writer.writerow([student_id, name, course, branch, date, status])
    
    print(f"CSV file '{filename}' generated.")

def generate_report_menu():
    while True:
        print("\nGenerate Report Menu:")
        print("1. Daily Report")
        print("2. Back to User Menu")

        report_choice = input("Enter your choice: ")

        if report_choice == "1":
            target_date = input("Enter the date (YYYY-MM-DD): ")
            generate_daily_report(target_date)
        elif report_choice == "2":
            break
        else:
            print("Invalid choice. Please choose again.")

def generate_daily_report(target_date):
    report = f"Daily Attendance Report for {target_date}:\n"
    report += "Student ID\tStatus\n"
    
    for student_id, student_info in student_manager.student_database.items():
        status = student_info["attendance"].get(target_date, "Absent")
        report += f"{student_id}\t\t{status}\n"
    
    print(report)

def generate_report_for_period(report, period_dates):
    report += "Student ID\tName\t"
    report += "\t".join(period_dates) + "\n"

    for student_id, student_info in student_manager.student_database.items():
        name = student_info.get("name", "Unknown")
        attendance_data = student_info.get("attendance", {})
        status_list = [attendance_data.get(date, "Absent") for date in period_dates]
        
        report += f"{student_id}\t\t{name}\t"
        report += "\t\t".join(status_list) + "\n"

    print(report)