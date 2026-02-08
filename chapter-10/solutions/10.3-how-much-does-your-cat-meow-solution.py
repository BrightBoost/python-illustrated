"""
A way to approach this:
1. Run the code, whoopsie, it crashes with ZeroDivisionError
2. Read traceback: "ZeroDivisionError: division by zero" at line with awake_hours calculation
3. Add print statement: print(f"Day: {log['day']}, Awake hours: {awake_hours}")
4. Discover: Wednesday has 24 hours of naps (8+6+9+1=24), making awake_hours = 0
5. Solution: Check if awake_hours == 0 before dividing
6. Use continue to skip days with no awake time
7. Track valid_days to calculate accurate average
8. Handle edge case: all days are full sleep (return None to avoid another division by zero)

Alternative debugging approach:
- Set breakpoint inside the for loop
- Step through each day's calculation
- Watch awake_hours variable, it will be 0 on Wednesday
"""

def average_meows(logs):
    total_meows_per_hour = 0
    valid_days = 0

    for log in logs:
        nap_hours = 0
        for nap in log["naps"]:
            nap_hours += nap
        awake_hours = 24 - nap_hours
        # BREAKPOINT HERE: Watch awake_hours, it becomes 0 on Wednesday
        # Why: Reveals the division by zero condition when cat sleeps all day
        if awake_hours == 0:
            print(f"{log['day']} was a full snooze day! Skipping...")
            continue # Skip this day to avoid division by zero
        
        total_meows_per_hour += log["meows"] / awake_hours
        valid_days += 1

    # Handle edge case: all days were full sleep
    if valid_days == 0:
        print("Your cat slept through the whole week. No data to average")
        return None

    return total_meows_per_hour / valid_days

logs = [
    {"day": "Monday", "naps": [1, 2, 5], "meows": 90},
    {"day": "Tuesday", "naps": [4, 3, 2], "meows": 75},
    {"day": "Wednesday", "naps": [8, 6, 9, 1], "meows": 9},
    {"day": "Thursday", "naps": [1, 1, 5, 7], "meows": 38},
    {"day": "Friday", "naps": [3, 3, 2, 8], "meows": 94},
    {"day": "Saturday", "naps": [4, 8, 3], "meows": 64},
    {"day": "Sunday", "naps": [3, 3, 2, 8], "meows": 37}
]

print("Average meows per awake hour:", average_meows(logs))

# Bug was: Wednesday has 24 hours of naps, causing division by zero
# Fix: Check if awake_hours == 0, skip that day with continue
# Improvement: Track valid_days for accurate average, handle all-sleep edge case