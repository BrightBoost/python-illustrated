
class LoginUser:
    def login(self, username, password):
        print(f"Logging in as {username}...")

    def welcome(self):
        print("Welcome to the portal!")

class Speaker:
    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    def speak(self):
        print(f"{self.name} is speaking about {self.topic}.")

    def welcome(self):
        print(f"Welcome to the conference, {self.name}!")

class LoggedInSpeaker(Speaker, LoginUser):
    pass

speaker = LoggedInSpeaker("Dr. Zia", "Quantum Computing for Cats")
speaker.welcome()


LoginUser.welcome(speaker)
Speaker.welcome(speaker)

class LoggedInSpeaker(Speaker, LoginUser):
    def welcome(self):
        print("Welcome, authenticated speaker! Enjoy the event and your coffee.")

speaker = LoggedInSpeaker("Dr. Zia", "Quantum Computing for Cats")
speaker.welcome()