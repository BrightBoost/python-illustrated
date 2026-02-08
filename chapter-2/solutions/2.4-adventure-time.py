# Create a variable for the current day of the month
current_day = 12  # You can change this number to test different days

# Use modulo to check if it's an adventure day (divisible by 5)
adventure_day = current_day % 5 == 0

# Print whether it's an adventure day or not
print("Adventure day?", adventure_day)
