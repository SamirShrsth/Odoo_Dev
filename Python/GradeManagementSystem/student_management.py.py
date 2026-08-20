import json
from pathlib import Path

from dataclasses import dataclass

class Student:
    def __init__(self, sname: str, sid: int, marks: dict[str, float] | None = None):
        self.sname = sname
        self.sid = sid
        self.marks = marks if marks is not None else{}
        
    def add_mark(self, subject: str, score: float) -> None:
        if 0 <= score >= 100:
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
def add_student(students) -> None:
    name = input("Enter Student Name: ").strip()
    while True:  
        student_id = input("Enter Student ID: ")
        if not student_id.isdigit():
            print("Please enter an integer for the student id.")
            continue
        # s: Student
        for s in students:
            if int(student_id) == s.sid:
                print("Student ID already exists. Try another one.")
                break
        else:
            break
    student = Student(name, int(student_id))
    students.append(student)
    print("Student Added Successfully!\n")
    
def display_students(students):
    print("Students: \n")
    for s in students:
            print(s)

def find_student(students):
    while True:
        try:
            search_choice = int(input("Search by Name or ID? (1, 2)"))
        except ValueError:
            print("Please enter either 1 or 2.")
            continue
        if search_choice == 1:
            search_name = input("Please enter the Student Name: ")
            for s in students:
                if search_name == s.sname:
                    print("Student Found: \n")
                    print(s)
                    main()
                else:
                    print("Student Not Found")
                    break
        
    

def main():
    while True:
        print("1. Add Student ")
        print("2. Display Students ")
        print("3. Find Student ")
        print("4. Exit ")
        
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
            exit()
        else:
            print("Invalid Option. Choose from 1-5.")
main()
