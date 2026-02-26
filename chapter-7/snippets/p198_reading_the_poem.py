# read() method
with open("p198_poem_for_wiesje.txt", "r") as file:
    content = file.read()
    print(content)

# realine() to read one line at a time
with open("p198_poem_for_wiesje.txt", "r") as file:
    while True:
        line = file.readline()
        if not line: # no more lines to read
            break
        print("Line read:", line.strip())

# readlines() to get all lines as a list
with open("p198_poem_for_wiesje.txt", "r") as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        print(f"Line {index+1}:", line.strip())

# Iterating over a file object
with open("poem_for_wiesje.txt", "r") as file:
    for line in file:
        print("Read line:", line.strip())