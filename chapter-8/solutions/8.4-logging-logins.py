from datetime import datetime

# Decorator function
def log(func):
    # Wrapper takes in an unknown amount of arguments
    def wrapper(self, *args):
        # determine time for log
        now = datetime.now()
        # Save the result of the method call in a variable while calling the function
        result = func(self, *args)
        # Write the login/logout attempt to the file.
        with open("logs.txt", "a") as file:
            file.write(f"{now}: {func.__name__} was called on {self.name}. Result: {result}\n")
        return result
    return wrapper

class User():
    # Define a constructor
    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._logged_in = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name.strip() == "":
            self._name = new_name
        else:
            print("Invalid name")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        # verifying password length
        if len(new_password) >= 8:
            self._password = new_password
        else:
            print("Password should at least be 8 characters long.")

    @property
    def logged_in(self):
        return self._logged_in

    @logged_in.setter
    def logged_in(self, bool):
        self._logged_in = bool

    # With @log decorated login method
    @log
    def login(self, entered_password):
        # No need to log in if you're already logged in
        if self.logged_in == True:
            print(f"{self.name} is already logged in.")
            # return statements for result in logs.txt
            return "Already logged in"
        # Only set logged_in to true if password is correct.
        if self.password == entered_password:
            self.logged_in = True
            print(f"{self.name} successfully logged in")
            return "Great success"
        else:
            print(f"Wrong password. Try again")
            return "Wrong password"
        
    # With @log decorated logout method
    @log
    def logout(self):
        # No use in logging out if you're not logged in
        if self.logged_in == False:
            print(f"{self.name} is already logged out.")
            return "Already logged out"
        else:
            self.logged_in = False
            print(f"{self.name} is logged out")
            return "Success"

user1 = User("Maaike91", "RightPassword!")
user2 = User("Imke97", "CorrectPassword?")

user1.login("RightPassword!")
user2.login("WrongPass")

user1.login("LoggingInAgain")
user1.logout()

user1.name = "MaaikeVanP"
user1.password = ""

user1.login("")
