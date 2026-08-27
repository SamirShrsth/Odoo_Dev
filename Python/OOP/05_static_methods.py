# static methods
# methods that belong to a class itself rather than an instance of the class(object)

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} : {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Accountant", "Cashier"]
        return position in valid_positions
    
print(Employee.is_valid_position("Manager"))
employee1 = Employee("Samir", "Manager")
print(employee1.get_info())