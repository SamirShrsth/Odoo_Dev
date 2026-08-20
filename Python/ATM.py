class Account:
    def __init__(self, name: str, pin: int, balance: float) -> None:
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transactions: list[str] = []

    def check_balance(self) -> None:
        print(f"Your current balance is Rs {self.balance:.2f}")

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        self.transactions.append(f"Deposited Rs {amount:.2f}")
        print(f"Deposited Rs {amount:.2f}. New balance: Rs {self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Withdrawal amount exceeds the account balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew Rs {amount:.2f}")
            print(f"Withdrew Rs {amount:.2f}. New balance: Rs {self.balance:.2f}")

    def show_transactions(self) -> None:
        if not self.transactions:
            print("No transactions yet.")
            return

        print("Recent transactions:")
        for transaction in self.transactions[-5:]:
            print(f"- {transaction}")

    def __str__(self) -> str:
        return f"{self.name}: Rs {self.balance:.2f}"


accounts = [
    Account("Samir", 1234, 10000),
    Account("Naayu", 7269, 50000),
    Account("Bipush", 7777, 100000),
]


def read_amount(prompt: str) -> float | None:
    try:
        return float(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None


def run_atm() -> None:
    while True:
        account_name = input("Enter your account name (or 'exit'): ").strip().lower()
        if account_name == "exit":
            print("Goodbye!")
            return

        account = next(
            (item for item in accounts if item.name.lower() == account_name),
            None,
        )
        if account is None:
            print("Account does not exist. Try again.")
            continue

        account_pin = input("Enter the PIN number: ").strip()
        if not account_pin.isdigit() or int(account_pin) != account.pin:
            print("Incorrect PIN.")
            continue

        print(f"Welcome {account.name}, you have been logged in.")
        while True:
            print("\n1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Exit")

            try:
                choice = int(input("Enter your choice (1-5): "))
            except ValueError:
                print("Please enter a number from 1 to 5.")
                continue

            if choice == 1:
                account.check_balance()
            elif choice == 2:
                amount = read_amount("Enter the amount to deposit: ")
                if amount is not None:
                    account.deposit(amount)
            elif choice == 3:
                amount = read_amount("Enter the amount to withdraw: ")
                if amount is not None:
                    account.withdraw(amount)
            elif choice == 4:
                account.show_transactions()
            elif choice == 5:
                print("Goodbye!")
                return
            else:
                print("Invalid option. Choose a number from 1 to 5.")


run_atm()