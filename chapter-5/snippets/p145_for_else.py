toys = ["all", "mouse", "string"]

for toy in toys:
    print("Checking:", toy)
    if toy == "feather":
        print("Found my feather! Time to play!")
        break # that skips the whole loop, including else
else:
    print("No feather found. I guess I'll nap instead.")





toys = ["ball", "feather", "string"]

for toy in toys:
    print("Checking:", toy)
    if toy == "feather":
        print("Found my feather! Time to play!")
        break
else:
    print("No feather found. I guess I'll nap instead.")