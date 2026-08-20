class Student:
    def __init__(self, sname: str, sid: int, marks: dict[str, float] | None = None):
        self.sname = sname
        self.sid = sid
        self.marks = marks if marks is not None else {}

    def add_mark(self, subject: str, score: float) -> None:
        if 0 <= score <= 100:
            self.marks[subject] = score
        else:
            print("Score must be between 0 and 100.")

    def calculate_average(self) -> float:
        if not self.marks:
            return 0.0
        total = sum(self.marks.values())
        return total / len(self.marks)

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

    def __str__(self) -> str:
        return f"Student ID: {self.sid}\nName: {self.sname}\nMarks: {self.marks}\nAverage: {self.calculate_average():.2f}\nGrade: {self.calculate_grade()}"


def add_student(students: list[Student]) -> None:
    name = input("Enter student name: ").strip()
    student_id = int(input("Enter student ID: "))
    students.append(Student(name, student_id))
    print("Student added successfully.")


def add_mark_to_student(students: list[Student]) -> None:
    student_id = int(input("Enter student ID: "))
    for student in students:
        if student.sid == student_id:
            subject = input("Enter subject name: ").strip()
            score = float(input("Enter score: "))
            student.add_mark(subject, score)
            print("Mark added successfully.")
            return
    print("Student not found.")


def display_students(students: list[Student]) -> None:
    if not students:
        print("No students available.")
        return

    for student in students:
        print("\n" + str(student))


def find_student(students: list[Student]) -> None:
    student_id = int(input("Enter student ID to search: "))
    for student in students:
        if student.sid == student_id:
            print("\n" + str(student))
            return
    print("Student not found.")


def main() -> None:
    students: list[Student] = []

    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add Student")
        print("2. Add Mark")
        print("3. Display Students")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            add_mark_to_student(students)
        elif choice == "3":
            display_students(students)
        elif choice == "4":
            find_student(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
