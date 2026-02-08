# Food in Wiesje's cupboards (in grams)
food_in_cupboards = 1500

# Wiesje's food intake per day (in grams)
food_per_day = 65  # But we all know it's more...

# Calculate how many full days the food will last using integer division
days_left = food_in_cupboards // food_per_day

# Print the result
print("Wiesje's food will last for", days_left, "full days.")

