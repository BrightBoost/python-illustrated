with open("filename.txt", "r") as file:
    pass # do something with file

with open("zia_diary.txt", "a") as file:
    file.write("Remember: never leave socks unattended.\n")
    file.write("Wiesje has claimed another victim.\n")


try:
    with open("zia_diary.txt", "r") as file:
        print(file.read())
except PermissionError:
    print("Back off, Wiesje! Zia's diary is private!")
except FileNotFoundError:
    print("Zia's diary is missing...")