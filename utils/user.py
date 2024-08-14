from utils.wallet import Wallet

class User:
    def __init__(self, userinfos="userinfos.txt"):
        self.wallet = Wallet()
        self.username = ""
        self.password = ""
        self.userinfos = userinfos

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username
    
    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password
    
    def change_password(self, current_password, new_password):
        if self.get_password() == current_password:
            self.set_password(new_password)
            return True
        return False
    
    def username_exists(self, username):
        try:
            with open(self.userinfos, "r") as file:
                for line in file:
                    if f"Username: {username}" in line:
                        return True
                return False
        except FileNotFoundError:
            return False
        
    def save_user(self):
        new_content = []
        user_found = False

        try:
            with open(self.userinfos, "r") as infile:
                content = infile.read()

            for line in content.splitlines():
                if line.startswith(f"Username: {self.get_username()}"):
                    line = (
                        f"Username: {self.get_username()}, "
                        f"Password: {self.get_password()}, "
                        f"Balance: {self.wallet.get_balance()}, "
                        f"TotalSpent: {self.wallet.get_total_spent()}, "
                        f"TotalLoss: {self.wallet.get_total_loss()}"
                    )
                    user_found = True
                new_content.append(line)

            if not user_found:
                new_content.append(
                    f"Username: {self.get_username()}, "
                    f"Password: {self.get_password()}, "
                    f"Balance: {self.wallet.get_balance()}, "
                    f"TotalSpent: {self.wallet.get_total_spent()}, "
                    f"TotalLoss: {self.wallet.get_total_loss()}"
                )

            with open(self.userinfos, "w") as outfile:
                outfile.write("\n".join(new_content) + "\n")

        except FileNotFoundError:
            with open(self.userinfos, "w") as outfile:
                outfile.write(
                    f"Username: {self.get_username()}, "
                    f"Password: {self.get_password()}, "
                    f"Balance: {self.wallet.get_balance()}, "
                    f"TotalSpent: {self.wallet.get_total_spent()}, "
                    f"TotalLoss: {self.wallet.get_total_loss()}"
                )

    def load_user(self, username, password):
        try:
            with open(self.userinfos, "r") as file:
                for line in file:
                    if line.startswith(f"Username: {username}"):
                        fields = line.split(", ")
                        stored_password = fields[1].split(": ")[1]
                        if stored_password == password:
                            self.set_username(username)
                            self.set_password(stored_password)
                            return True
                        
        except FileNotFoundError:
            return False
        return False      