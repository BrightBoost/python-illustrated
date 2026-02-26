# Question 8
def average_time(laps):
    time = 0
    for lap in laps:
        lap += time
    return time / len(laps)

laps = [60, 62, 58]
print("Average time:", average_time(laps))
