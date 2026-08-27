class Student:
    # class variable
    batch_year = 2022
    # similar to constructors in java
    def __init__(self, name: str, age: int):
        # instance variables
        self.name = name
        self.age = age
    # methods
    def get_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Batch: {Student.batch_year}")
    # dunder method
    def __str__(self):
        return f"{self.name} is {self.age}yo."
        
student1: Student = Student("Samir", 21)
print(student1)
student1.get_info()