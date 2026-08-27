class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")

# class Dog inherits Animal
class Dog(Animal):
    def speak(self):
        print("Woof!")
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
dog = Dog("Johnny")
dog.eat()
dog.speak()
dog.sleep()
cat = Cat("Delilah")
print()
cat.eat()
cat.speak()
cat.sleep()