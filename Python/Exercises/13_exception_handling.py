# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, ValueError, TypeError)
#             (try, except, finally)
while True:
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        try:
            print(num1/num2)
            break
        except ZeroDivisionError:
            print("Error: Cannot Divide By Zero!")
            continue
    except ValueError:
        print("Error: Please enter a number")
        continue
    finally:
        print("Thank You!")