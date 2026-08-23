class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand=brand
        self.horsepower=horsepower
    
    def drive(self) -> None:
        print(f"{self.brand} is driving")
    
    def get_info(self) -> None:
        print(f"{self.brand} has {self.horsepower} horsepower")
        
    def __str__(self) -> str:
        return f'{self.brand}, {self.horsepower}hp'
    
    def __add__(self, other)-> str:
        return f'{self.brand} & {other.brand}'
    
        
    
toyota : Car = Car('Toyota', 500)
volkswagen : Car = Car('Volkswagen', 600)

toyota.drive()
toyota.get_info()

volkswagen.drive()
volkswagen.get_info()

# possible because of the __str__ dunder method
print(f"Toyota : {toyota}")
# possible because of the __add__ dunder method
print(f"Cars: {toyota + volkswagen}")