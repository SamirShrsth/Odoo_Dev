import json
from pathlib import Path

from dataclasses import dataclass

class Student:
    def __init__(self, sname: str, sid: int, marks: dict[str, float] | None = None):
        self.sname = sname
        self.sid = sid
        self.marks = marks if marks is not None else{}
        
    def add_mark(self, subject: str, score: float) -> None:
        if 0 <= score <= 100:
            self.marks[subject] = score
        else:
            print("Score must be within 0-100.")
            
    def calculate_average(self) -> float:
        if not self.marks:
            return 0
        total = sum(self.marks.values())
        average = total / len(self.marks)
        return average
    
    def calculate_grade(self) -> str:
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
        
    def __str__(self):
        return f"Student Id: {self.sid} \nStudent Name: {self.sname.capitalize()} \nStudent Marks: {self.marks}\n"

students = []


def save_students(students : list[Student], file_path: str | Path = "./Python/GradeManagementSystem/students.json"):
    data = [
        {"name": student.sname, "id": student.sid, "marks": student.marks}
        for student in students
    ]
    path = Path(file_path)
    path.write_text(json.dumps(data, indent=4), encoding="utf-8")
    
def load_students(
    file_path: str | Path = "./Python/GradeManagementSystem/students.json",
) -> list[Student]:
    path = Path(file_path)
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return [
        Student(item["name"], item["id"], item.get("marks", {}))
        for item in data
    ]

def add_student(students: list[Student]) -> None:
    name = input("Enter Student Name: ").strip()
    while True:  
        student_id = input("Enter Student ID: ")
        if not student_id.isdigit():
            print("Please enter an integer for the student id.")
            continue
        # s: Student
        for student in students:
            if int(student_id) == student.sid:
                print("Student ID already exists. Try another one.")
                break
        else:
            break
    student = Student(name, int(student_id))
    students.append(student)
    print("Student Added Successfully!\n")


def add_mark_to_student(students) -> None:
    while True:
        try:
            student_id = int(input("Enter the student ID: "))
        except ValueError:
            print("Please enter an integer.")
            continue
            
        for student in students:
            if student_id == student.sid:
                print(student)
                student_subject = input("Enter the subject: ")
                student_score = float(input(f"Enter the marks for {student_subject}: "))
                student.add_mark(student_subject, student_score)
                print("Marks Added.")
                return
        print("Student ID doesn't Exist")
        continue
        

def display_students(students) -> None:
    print("Students: \n")
    for student in students:
            print(student)

def find_student(students) -> None:
    while True:
        try:
            search_choice = int(input("Search by Name or ID? (1, 2): "))
        except ValueError:
            print("Please enter either 1 or 2.")
            continue
        if search_choice == 1:
            search_name = input("Please enter the Student Name: ")
            for student in students:
                if search_name == student.sname:
                    print("Student Found: \n")
                    print(student)
                    # main()
                    return
            print("Student Not Found. ")
                
        elif search_choice == 2:
            search_id = int(input("Enter the student ID: "))
            for student in students:
                if search_id == student.sid:
                    print("Student Found: \n")
                    print(student)
                    return
                    # main()
            print("Student Not Found. ")
                
        else:
            print("Invalid Option")
            
def main():
    students.extend(load_students())
    while True:
        print("1. Add Student ")
        print("2. Display Students ")
        print("3. Find Student ")
        print("4. Add Marks ")
        print("5. Exit ")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid choice(1-2)") 
            continue
        if choice == 1:
            add_student(students)
        elif choice == 2:
            display_students(students)
        elif choice == 3:
            find_student(students)
        elif choice == 4:
            add_mark_to_student(students)
        elif choice == 5:
            save_students(students)
            print("Students saved successfully. Goodbye!")
            return
        else:
            print("Invalid Option. Choose from 1-5.")
main()
