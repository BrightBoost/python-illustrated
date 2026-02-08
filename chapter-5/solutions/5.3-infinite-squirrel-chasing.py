# Infinite squirrel chasing
while True:
    print("Wiesje chases the squirrel!")
# Control+c in terminal to stop infinite loop
# Remove or comment out this infinite loop before continuing

# Squirrel chasing while wiesje has energy
wiesje_energy = 10

while wiesje_energy > 0:
    print("Wiesje chases the squirrel!")
    wiesje_energy -= 1

print("Wiesje is too tired and gives up.")

# Bonus challenge
wiesje_energy = 5
squirrel_energy = 100

while wiesje_energy > 0 and squirrel_energy > 0:
    print("Wiesje chases the squirrel...")
    wiesje_energy -= 1
    squirrel_energy -= 1

if squirrel_energy == 0 and wiesje_energy == 0:
    print("Wiesje catches the squirrel just before collapsing!")
elif squirrel_energy == 0:
    print("Wiesje caught the squirrel!")
else:
    print("Wiesje is too tired and gives up.")
