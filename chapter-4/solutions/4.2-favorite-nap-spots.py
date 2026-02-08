fav_nap_spots = ["window", "cardboard box", "human's lap", "luxurious cat bed"]

# Remove the luxurious cat bed from the list (last item)
fav_nap_spots.pop()

# Add "keyboard" as first item on the list
fav_nap_spots.insert(0, "keyboard")

# Insert "sunbeam on the floor" as third item on the list
fav_nap_spots.insert(2, "sunbeam on the floor")

# Add "Wiesje's bed" to the end of the list
fav_nap_spots.append("Wiesje's bed")

# Check if "Check for "human bed" and add if needed"
if "human bed" not in fav_nap_spots:
    fav_nap_spots.append("human bed")

# Slice the top three nap spots
top_three_nap_spots = fav_nap_spots[0:3]
print(top_three_nap_spots)

# Bonus challenge: Swap elements on a list
fav_nap_spots[1], fav_nap_spots[3] = fav_nap_spots[3], fav_nap_spots[1]

# Update top three after swapping items
top_three_nap_spots = fav_nap_spots[0:3]


print(fav_nap_spots)
print(top_three_nap_spots)
