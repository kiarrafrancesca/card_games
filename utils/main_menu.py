from utils.user_manager import UserManager
from utils.user import User
from utils.wallet import Wallet

usermanager = UserManager()
user = User()

def menu():
    while True:
        try:
            print("<----------------------------------->")
            print("|             Welcome!              |")
            print("<----------------------------------->")
            print("| [1] Sign-up                       |")
            print("| [2] Log-in                        |")
            print("<----------------------------------->")
            print("| [3] Exit                          |")
            print("<----------------------------------->")    

            choice = int(input("Enter your choice: "))

            if choice == 1:
                usermanager.clear_screen()
                sign_up()
            elif choice == 2:
                usermanager.clear_screen()
                log_in()
            elif choice == 3:
                print("\nExiting...")
                quit()
            else:
                print("Please enter a valid choice from the menu.")

        except ValueError:
            print("Please enter a valid choice from the menu.")

def sign_up():
    print("<----------------------------------->")
    print("|             SIGN-UP               |")
    print("<----------------------------------->")

    while True:
        username = usermanager.username_input()

        if username == "x" or username == "X":
            usermanager.clear_screen()
            return
        
        if not user.username_exists(username):
            break
        print("Username already exists.")
    
    user.set_username(username)

    password = usermanager.password_input()
    user.set_password(password)

    user.save_user()

    usermanager.clear_screen()
    print(f"Sign-up successful! Welcome, {username}!")
    usermanager.press_return()

def log_in():
    print("<----------------------------------->")
    print("|             LOG-IN                |")
    print("<----------------------------------->")   

    while True:
        username = usermanager.username_input()

        if username == "x" or username == "X":
            usermanager.clear_screen()
            return
        
        password = usermanager.password_input()

        if user.load_user(username, password):
            usermanager.clear_screen()
            print(f"Login successful! Welcome back, {username}!")
            usermanager.press_return()
            main_menu(user)
        else:
            usermanager.clear_screen()
            print("Invalid username or password.")
            usermanager.press_return()

def main_menu(user):
    while True:
        try:
            print("<----------------------------------->")
            print("|        Welcome to User Menu!      |")
            print("<----------------------------------->")
            print("| Select an option:                 |")
            print("| [1] Account Profile               |")
            print("| [2] Games                         |")
            print("| [3] Wallet                        |")
            print("<----------------------------------->")
            print("| [4] Log out                       |")
            print("<----------------------------------->")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                accprofile = AccountProfile(user)
                accprofile.account_profile()
            elif choice == 2:
                pass
            elif choice == 3:
                wallet = Wallet()
                wallet.view_wallet()
            elif choice == 4:
                print("Logging out...")
                quit()
            else:
                print("Please enter a valid choice from the menu.")

        except ValueError:
            print("Please enter a valid choice from the menu.")

class AccountProfile:
    def __init__(self):
        self.user = User()
        self.usermanager = UserManager()
        self.wallet = Wallet()
                
    def account_profile(self):
        while True:
            try:
                print("+---------------------------------------+")
                print("|             Account Profile           |")
                print("+---------------------------------------+")
                print(f" Username:              {self.user.get_username()}")
                print(f" Total amount spent:    {self.wallet.get_total_spent()}")
                print(f" Total amount loss:     {self.wallet.get_total_loss()}")
                print(f" Current balance:       {self.wallet.get_balance()}")
                print("+---------------------------------------+")
                print("| [1] Change password                   |")
                print("| [2] Return to user menu               |")
                print("+---------------------------------------+")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.usermanager.clear_screen()
                    self.change_pass()
                elif choice == 2:
                    self.usermanager.clear_screen()
                    return
                else:
                    self.usermanager.clear_screen()
                    print("Please enter a valid choice from the meunu.")

            except ValueError:
                print("Please enter a valid choice from the menu.")   

    def change_pass(self):
        input("Enter current password for verification: ")
        old_password = self.usermanager.password_input()

        if self.user.load_user(self.user.get_username(), old_password):
            self.usermanager.clear_screen()
            print("<----------------------------------->")
            print("|           CHANGE PASSWORD         |")
            print("<----------------------------------->")
            print()

            new_password = self.usermanager.password_input()
            self.user.set_password(new_password)

            print("Password changed successfully!")
            self.usermanager.press_return()
            return
        
        else:
            self.usermanager.clear_screen()
            print("Incorrect password.")
            self.usermanager.press_return()