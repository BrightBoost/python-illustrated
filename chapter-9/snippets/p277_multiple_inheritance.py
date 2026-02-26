class LoginUser:
    def login(self, username, password):
        print(f"Logging in as {username}...")

class Speaker:
    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    def speak(self):
        print(f"{self.name} is speaking about {self.topic}.")

class LoggedInSpeaker(Speaker, LoginUser):
    def upload_slides(self, slides):  
        pass

s = LoggedInSpeaker("Dr. Zia", "Quantum Computing for Cats")
s.speak()
s.login("dr_zia", "Purrsecure123!")
