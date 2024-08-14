from utils.user import User
from utils.user_manager import UserManager

class Wallet:
    def __init__(self, user):
        self.usermanager = UserManager()
        self.user = user
        self.current_user = {
                "username": self.user.get_username(),
                "password": self.user.get_password(),
                "balance": 0.0,
                "total_spent": 0.0,
                "total_loss": 0.0
            }

    def get_balance(self):
        return self.current_user["balance"]

    def get_total_spent(self):
        return self.current_user["total_spent"]

    def get_total_loss(self):
        return self.current_user["total_loss"]

    def add_balance(self, amount):
        self.current_user["balance"] += amount
        self.user.save_user()

    def subtract_balance(self, amount):
        self.current_user["balance"] -= amount
        self.user.save_user()

    def add_total_spent(self, amount):
        self.current_user["total_spent"] += amount
        self.user.save_user()

    def add_total_loss(self, amount):
        self.current_user["total_loss"] += amount
        self.user.save_user()

    def view_wallet(self):
        while True:
            try:
                print("+---------------------------------------+")
                print("|                WALLET                 |")
                print("+---------------------------------------+")
                print(f" Current balance: $ {self.get_balance()}")
                print("+---------------------------------------+")
                print("| [1] Top-up                            |")
                print("| [2] Withdraw                          |")
                print("+---------------------------------------+")
                print("| [3] Exit                              |")
                print("+---------------------------------------+")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.usermanager.clear_screen()
                    self.top_up()
                elif choice == 2:
                    self.usermanager.clear_screen()
                    self.withdraw()
                elif choice == 3:
                    self.usermanager.clear_screen()
                    return
                else:
                    self.usermanager.clear_screen()
                    print("Please enter a valid choice from the menu.")

            except ValueError:
                print("Please enter a valid choice from the menu.")


    def top_up(self):
        while True:
            try:
                print("+---------------------------------------+")
                print("|                TOP-UP                 |")
                print("+---------------------------------------+")
                
                amount = float(input("Enter amount to top-up: "))

                if amount <= 0:
                    self.usermanager.clear_screen()
                    print("Amount must be greater than 0.")
                    continue
                else:
                    self.add_balance(amount)
                    print("Successfully updated balance!")
                    self.usermanager.press_return()
                    return
                
            except ValueError:
                print("Please enter a valid amount.")

    def withdraw(self):
        while True:
            try:
                print("+---------------------------------------+")
                print("|               WITHDRAW                |")
                print("+---------------------------------------+")
                
                amount = float(input("Enter amount to withdraw: "))

                if amount <= 0:
                    self.usermanager.clear_screen()
                    print("Amount must be greater than 0.")
                    continue
                elif amount > self.get_balance():
                    self.usermanager.clear_screen()
                    print("You do not have enough balance.")
                else:
                    self.subtract_balance(amount)
                    print("Successfully updated balance!")
                    self.usermanager.press_return()
                    return
                
            except ValueError:
                print("Please enter a valid amount.")