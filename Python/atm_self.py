import time

class Account:
    def __init__(self, name: str, pin: int, balance: float) -> None:
        self.name = name
        self.pin = pin
        self.balance = balance
    
    def check_balance(self) -> None:
        print(f"Your Current Balance is Rs {self.balance}")
    
    def deposit(self, amount) -> None:
        if(amount < 0):
            print("Cannot deposit a negative amount. Try again!")
        else:
            print(f"Previous balance = Rs {self.balance}")
            self.balance += amount
            print(f"Credited amount = Rs {amount}")
            print(f"Final Balance = Rs {self.balance}")
    
    def withdraw(self, amount) -> None:
        if(amount < 0):
            print("Cannot withdraw a negative amount. Try again!")
        elif(amount > self.balance):
            print("Withdraw amount exceeds the account balance!")
        else:
            print(f"Previous Balance = Rs {self.balance}")
            self.balance -= amount
            print(f"Debited Amount = Rs {amount}")
            print(f"Final Balance = Rs {self.balance}")
    
    def __str__(self):
        pass
    
accounts = []
    
samir : Account = Account("Samir", 1234, 10000)
naayu : Account = Account("Naayu", 7269, 50000)
bipush : Account = Account("Bipush", 7777, 100000)


accounts.append(samir)
accounts.append(naayu)
accounts.append(bipush)

# for x in accounts:
#     print(x.name)


for x in accounts:
    while True:
        acc_name = input("Enter your Account Name: ")
        if acc_name == (x.name).lower():
            while True:
                acc_pin = int(input("Enter the pin number: "))
                if acc_pin == x.pin: 
                    
                    print(f"Welcome {x.name}, You have been logged in.")
                    print("1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Exit")
                    while True:
                        choice = int(input("Enter your choice (1-4): "))
                        
                        if choice == 1:
                            x.check_balance()
                        elif choice == 2:
                            deposit_amount = float(input("Enter the amount to deposit: "))
                            x.deposit(deposit_amount)
                        elif choice == 3:
                            withdraw_amount = float(input("Enter the amount to withdraw: "))
                            x.withdraw(withdraw_amount)
                        elif choice == 4:
                            print("Exiting..")
                            time.sleep(1)
                            exit()
                        else:
                            print(f"{choice} is not a valid option.")
                else:
                        print("Incorrect Pin. Try again") 
        else:
            print("Account Does not Exist!")            