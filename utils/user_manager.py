from utils.user import User
import os

class UserManager:
    def __init__(self):
        self.current_user = User()

    def clear_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def press_return(self):
        input("Press 'enter' to return.")
        self.clear_screen()

    def username_input(self):
        while True:
            username = input("Enter a username (enter 'x' to exit): ")

            if len(username) >= 4:
                return username
            print("Username must be at least 4 characters long.")

    def password_input(self):
        while True:
            password = input("Enter a password: ")

            if len(password) < 6:
                print("Password must be at least 6 characters long.")
                continue

            confirm_password = input("Confirm password: ")

            if confirm_password != password:
                print("Password do not match, try again.")
            else:
                return password 