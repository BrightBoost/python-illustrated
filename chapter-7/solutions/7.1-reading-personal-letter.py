try:
    with open("letter.txt", "r") as  file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Oops, the letter can't be found.")