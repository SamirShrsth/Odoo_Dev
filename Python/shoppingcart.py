users = [{"name": "samir", "balance": 100000}, {"name": "bipasana", "balance": 200000}]
username = input("Enter your username: ").strip().lower()
found = False

for user in users:
    if user["name"] == username:
        found = True
        items = {"macbook": 100000, "dell": 20000}
        print(f"Available Laptops: {', '.join(items.keys())}")

        item = input("What laptop do you want? ").strip().lower()
        quantity = int(input(f"How many {item} laptops do you want? "))

        if item in items:
            price = items[item]
            total_cost = price * quantity
            print(f"The total cost for {quantity} {item} laptop(s) is Rs.{total_cost}")
        else:
            print("Item not found")

        choice = input("Would you like to purchase? (1=Yes, 2=No): ")
        if choice == "1":
            if user["balance"] >= total_cost:
                print("Items purchased!")
                user["balance"] = user["balance"] - total_cost
                print(f'Your remaining balance is Rs.{user["balance"]}')
            else:
                print(f'Insufficient balance! Current balance = Rs.{user["balance"]}')
        elif choice == "2":
            print("Purchase Cancelled")

if not found:
    print("User not found")