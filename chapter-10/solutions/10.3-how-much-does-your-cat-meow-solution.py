def average_meows(logs):
    total_meows_per_hour = 0
    valid_days = 0

    for log in logs:
        nap_hours = 0
        for nap in log["naps"]:
            nap_hours += nap
        awake_hours = 24 - nap_hours
        if awake_hours == 0:
            print(f"{log['day']} was a full snooze day! Skipping...")
            continue
        total_meows_per_hour += log["meows"] / awake_hours
        valid_days += 1

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