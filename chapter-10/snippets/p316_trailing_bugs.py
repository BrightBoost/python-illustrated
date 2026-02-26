def total_distance(*segments):
    total = 0

    for length, unit in segments:
        if unit.lower() == "M":
            total += length
        elif unit.lower() == "km":
            total += length / 1000

    print("Total distance:", total, "meters")


total_distance(
    (2.5, "km"),
    (400, "M"),
    (1.0, "km"),
    (800, "m"),
    (1.3, "KM"),
    (900, "m "),
    (1.1, "km")
)
