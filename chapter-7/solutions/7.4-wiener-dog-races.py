import csv
# Count the participants
def count_participants():
    try:
        with open("wiener_dog_race_results.csv", "r") as file:
            content = csv.reader(file)
            data = list(content)[1:] # Takes the rows of content as a list but skips the header by starting at index 1

            # Determine the amount of participants using the len() function
            print(f"{len(data)} dachshunds participated in this race.")

            # Dealing with empty rows in the list
            counter = 0
            for row in data:
                if len(row) >= 2 and row[0].strip() and row[1].strip():
                    counter += 1
            print(f"{counter} dachshunds participated in this race.")
    except FileNotFoundError:
        print("Could not find file with race data")

# Calling the function
count_participants()

# Function to add new results
def add_results(name, time):
    name_exists = False
    results = [name, time]

    # Check if name is already in results
    try:
        with open("wiener_dog_race_results.csv", "r") as file:
            content = csv.reader(file)
            for row in content:
                if len(row) and row[0] == name:
                    name_exists = True
                    break

        # if name does not exist in file, add results
        if not name_exists:
            with open("wiener_dog_race_results.csv", "a", newline="") as file:
                content = csv.writer(file)
                content.writerow(results)
        else:
            print(f"{name} is already in the file")
    except FileNotFoundError:
        print("Could not find file with race data")

add_results("Wiesje", 42.0)

# Rank the wieners
def rank_the_wieners():
    try:
        with open("wiener_dog_race_results.csv", "r") as file:
            content = csv.reader(file)
            data = list(content)[1:] # skip the header
            data = [row for row in data if len(row) == 2 and row[0].strip() and row[1].strip()] # makes sure you only sort valid entries

            for i in range(len(data)): # for each item in the data list...
                data[i][1] = float(data[i][1]) # convert the time to float (to enable comparison)

            for i in range(len(data)):
                for j in range(i + 1, len(data)):
                    # compare finish times and swap rows if they are in the wrong order
                    if data[i][1] > data[j][1]: 
                        data[i], data[j] = data[j], data[i]

        # save the sorted race results to a new file
        with open("wiener_dog_race_results_sorted.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Finish Time (seconds)'])  # Write the header
                writer.writerows(data)  # Write the sorted data rows

    except FileNotFoundError:
        print("Could not find file with race data.")

rank_the_wieners()

# Determine the winner
def determine_winner():
    try:
        # open the file with sorted results
        with open("wiener_dog_race_results_sorted.csv", "r") as file:
            content = csv.reader(file)
            data = list(content)
            winner = data[1] # take the second row of the file, just below the header, which contains the dachshund with the fastest time.
            print(f"Dachshund {winner[0]} wins the race with an astonishing time of {winner[1]} seconds!")
    except FileNotFoundError:
        print("There is no file with sorted race results found.")

# Call the function
determine_winner()
