# For bonus challenge
import random
import time

# Open and create a file named note_to_self.txt
with open("note_to_self.txt", "w") as file:
    # Write a few lines of empowering words
    file.write("Curiosity rarely kills a cat.\n")
    file.write("Just keep purring.\n")
    file.write("Be patient with yourself.\n")
    file.write("Take a break, but don't quit.\n")
    file.write("If all fails, blame Wiesje.\n")

# Read the file and print each line numbered individually
try:
    with open("note_to_self.txt", "r") as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            print(f"{index + 1}. {line.strip()}")
except:
    print("Something went wrong trying to read the file.")

# Bonus challenge: A function for a random piece of advice
def ask_oracle():
    intros = [
    "Nine lives taught me this:",
    "I gazed into the void between naps and found this:",
    "With a flick of my tail, I reveal:",
    "I have knocked over the mug of fate. Here's what spilled out:"
]
    in_need_of_advice = input("Do you need advice? ")
    if in_need_of_advice.lower() == "yes":
        try:
            with open("note_to_self.txt", "r") as file:
                lines = file.readlines()
                advice = random.choice(lines)
                time.sleep(1)
                print("Hmm...")
                time.sleep(2)
                print(random.choice(intros), advice.strip())
        except:
            print("Something went wrong trying to find my wisdom")
    elif in_need_of_advice.lower() == "no":
        print("Are you sure?")
        ask_oracle()
    else:
        print("I'm sorry, I only understand \"yes\" and \"no\"")
        ask_oracle()

# Calling the function
ask_oracle()
