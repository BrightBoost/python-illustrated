"""
A way to approach this:
1. Run the code, it executes but... total distance seems wrong (should be  around 8000m, not tiny number)
2. Add print statements inside the loop:
    print(f"Segment: {length} {unit}, Current total: {total}")
3. Observe:
    - Some segments aren't being added (case sensitivity issue)
    - Kilometers are divided by 1000 instead of multiplied (math error)
    - Some segments with trailing spaces don't match (whitespace issue)
4. Identify 3 bugs:
    a) unit.lower() == "M", lowercase "m" never equals uppercase "M"
    b) total += length / 1000, should multiply to convert km to meters
    c) Trailing whitespace in "m " doesn't match "m"
5. Fix all three: use .lower().strip() and correct the multiplication

Alternative debugging approach:
- Set breakpoint inside for loop
- Step through each segment
- Watch which if/elif branches execute
- Notice some segments are skipped entirely
"""

def total_distance(*segments):
    total = 0
    
    # BREAKPOINT HERE: Step through to see which condition executes for each segment
    # Why: Reveals that some segments don't match either condition due to case/whitespace
    for length, unit in segments:
        # Print for debugging: print(f"Processing: {length} {unit!r}")
        if unit.lower().strip() == "m": # Fixed: added .lower() and .strip()
            total += length  # Meters - add directly
        elif unit.lower().strip() == "km": # Fixed: added .lower() and .strip()
            total += length * 1000 # Fixed: multiply by 1000, not divide

    print("Total distance:", total, "meters")

total_distance(
    (2.5, "km"),   # Was being divided instead of multiplied
    (400, "M"),    # Uppercase M wasn't matching lowercase "m"
    (1.0, "km"),   
    (800, "m"),    # This one worked in original
    (1.3, "KM"),   # Mixed case wasn't matching
    (900, "m "),   # Trailing space wasn't matching
    (1.1, "km")
)

# Three bugs fixed:
# 1. Case sensitivity: unit.lower() == "M" never matched, added .lower() to both conditions
# 2. Wrong conversion: divided by 1000 instead of multiplying, changed to * 1000
# 3. Whitespace: "m " didn't match "m", added .strip() to both conditions
# Expected output: Total distance: 8000.0 meters
