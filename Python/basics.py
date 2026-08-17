# print
print("Hello World")

# array with a for loop
nums = [1,2,3,4]
for i in nums:
    print(i)

# function definiion
def sayHello():
    print("Hello " + user1)
    print(f"You are {age} years old.")
    
print("Sign up: ")

# user input
user = input("Choose your username: ")
age = int(input("Enter your age: "))
print("You have been signed up!")

user1 = input("Enter your username: ")
# if statement
if user1 == user:
    # calling function sayHello()
    sayHello()
    

# type casting 
num1 = 2.5
num2 = 3
num3 = int(num1)

print(f"Before type cast, SUM = {num1+num2}")
print(f"After type cast, SUM = {num2+num3}")