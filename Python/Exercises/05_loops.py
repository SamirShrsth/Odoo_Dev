found = True
while found:
    user_input = input("Enter a number (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        found = False
    else:
        try:
            number = float(user_input)
            print(f"You entered: {number}")
        except ValueError:
            print("That's not a valid number. Please try again.")
    