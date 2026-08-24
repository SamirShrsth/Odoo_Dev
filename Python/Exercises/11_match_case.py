# match-case similiar to switch-case 

def day_of_the_week(day):
    match day:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case _:
            print("Not a valid day")
            
# using OR ( | ) in match-case
def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            print(f"{day} is a weekend")
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print(f"{day} is not a weekend")
day_of_the_week(4)
is_weekend("Monday")