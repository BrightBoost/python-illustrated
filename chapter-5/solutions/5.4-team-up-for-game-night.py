friends = ["Max", "Louise", "Jacob", "Sam", "Farah", "Selim"]
team_a = []
team_b = []

for index in range(len(friends)):
    if index % 2 == 0: # Using modulo to select even indices
        team_a.append(friends[index])
    else:
        team_b.append(friends[index])

print("Team A:")
for friend in team_a:
    print(friend)

print("\nTeam B:") # \n to create a line of whitespace between the two teams
for friend in team_b:
    print(friend)

