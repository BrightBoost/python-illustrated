workouts = {
    "Zia": {
        "bench_press": {"weight": 5, "sets": 3, "reps": 10},
        "bicep_curls": {"weight": 2, "sets": 3, "reps": 10},
        "box_jumps": {"weight": 0, "sets": 2, "reps": 10},
        "deadlifts": {"weight": 10, "sets": 2, "reps": 1},
        "kettle_bell_swings": {"weight": 2, "sets": 3, "reps": 10},
        "lateral_raises": {"weight": 1, "sets": 3, "reps": 10},
        "stair_climber": {"minutes": 10}
    },
    "Wiesje": {
        "bench_press": {"weight": 5, "sets": 1, "reps": 1},
        "leg_extension": {"weight": 1, "sets": 2, "reps": 5},
        "planking": {"minutes": 5},
        "zoomies": {"minutes": 2}
    }
}

# Loop through the workouts dictionary for each gym member
for member, exercises in workouts.items():
    print(f"{member}'s workout:")
    # Loop through each exercise of the current member
    for exercise, details in exercises.items():
        if "minutes" in details:
            print(f"- {exercise}: {details['minutes']} minutes")
        else:
            print(f"- {exercise}: weight {details['weight']}kg, {details['sets']} sets of {details['reps']} reps")
    print()

# Loop through the workouts dictionary for each gym member
for member, exercises in workouts.items():
    total_weight = 0  # Initialize the total weight to 0 for each member

    # Loop through each exercise of the current member
    for exercise, details in exercises.items():
        if "weight" in details: # Only add up the weight if the exercise involves lifting weight (if it has a "weight" key)
            total_weight += details["weight"] * details["sets"] * details["reps"]

    print(f"Total weight lifted by {member}: {total_weight}kg")
