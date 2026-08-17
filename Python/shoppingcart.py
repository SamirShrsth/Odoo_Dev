
items = {"macbook": 100000, "dell": 20000}
print(f"Available Laptops:  {', '.join(items.keys())}")
item = input("What laptop do you want? ").lower()
quantity = int(input(f"How many {item} laptops do you want? "))


if item in items:
    price = items[item]
    print(f"The total cost for {quantity} {item} laptop is {price*quantity}")
else:
    print("Item not found")

