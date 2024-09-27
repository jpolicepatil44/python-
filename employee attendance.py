

import datetime
import calendar

class Employee:
    def __init__(self, id, name):
        
        self.name = name
        self.attendance = {}

    def mark_attendance(self, date, status):
        self.attendance[date] = status

    def view_attendance(self):
        for date, status in self.attendance.items():
            print(f"{date}: {status}")

    def calculate_absenteeism(self):
        total_days = 0
        absent_days = 0
        for month in range(1, 13):
            num_days = calendar.monthrange(datetime.date.today().year, month)[1]
            total_days += num_days
            for day in range(1, num_days + 1):
                date = datetime.date(datetime.date.today().year, month, day)
                if date in self.attendance and self.attendance[date] == "Absent":
                    absent_days += 1
                    if total_days==0:
                        absenteeism_rate=0
                    else:
                        absenteeism_rate = (absent_days / total_days) * 100
        return absenteeism_rate

class AttendanceSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, id, name):
        self.employees[id] = Employee(id, name)

    def mark_attendance(self, id, date=None, status="Present"):
        if date is None:
            date = datetime.date.today()
        if id in self.employees:
            self.employees[id].mark_attendance(date, status)
        else:
            print("Employee not found.")

    def view_attendance(self, id):
        if id in self.employees:
            print(f"Attendance Record for {self.employees[id].name}:")
            self.employees[id].view_attendance()
        else:
            print("Employee not found.")

    def generate_report(self, id):
        if id in self.employees:
            print(f"Attendance Report for {self.employees[id].name}:")
            self.employees[id].view_attendance()
            absenteeism_rate = self.employees[id].calculate_absenteeism()
            print(f"Absenteeism Rate: {absenteeism_rate}%")
        else:
            print("Employee not found.")

def main():
    attendance_system = AttendanceSystem()

    while True:
        print("\nEmployee Attendance System")
        print("1. Add Employee")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            attendance_system.add_employee(id, name)
        elif choice == "2":
            id = input("Enter employee ID: ")
            date = input("Enter date (YYYY-MM-DD) or press enter for today: ")
            if date == "":
                date = datetime.date.today()
            else:
                date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            status = input("Enter attendance status (Present/Absent): ")
            attendance_system.mark_attendance(id, date, status)
        elif choice == "3":
            id = input("Enter employee ID: ")
            attendance_system.view_attendance(id)
        elif choice == "4":
            id = input("Enter employee ID: ")
            attendance_system.generate_report(id)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()


