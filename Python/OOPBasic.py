class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand=brand
        self.horsepower=horsepower
    
    def drive(self) -> None:
        print(f"{self.brand} is driving")
    
    def get_info(self) -> None:
        print(f"{self.brand} has {self.horsepower} horsepower")
        
    
toyota : Car = Car('Toyota', 500)
volkswagen : Car = Car('Volkswagen', 600)

toyota.drive()
toyota.get_info()

volkswagen.drive()
volkswagen.get_info()