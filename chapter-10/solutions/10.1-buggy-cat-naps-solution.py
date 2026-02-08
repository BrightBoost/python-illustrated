"""
A way to approach this:
1. Run the code and observe the output: hmmm, total is 8.5 instead of expected 10.5
2. Use print statements to see what values are being added or add a breakpoint in the while loop to inspect counter and total values:
    - Print the counter value
    - Print the value being added each iteration
3. Notice that the first nap (2 hours) is never added
4. Identify the bug: while loop starts at counter=1, skipping index 0

Fix in the while loop OR use a for loop to eliminate indexing issues entirely (even cleaner solution)
"""

def nap_time(hours_list):
    total = 0
    # BREAKPOINT at the for loop: Step through to see which values get added
    # Why: This reveals that index 0 is skipped (counter starts at 1)
    for nap in hours_list:
        total += nap
    return total


cat_naps = [2, 3, 1.5, 4]
print("Total nap time:", nap_time(cat_naps))

# Expected output: 10.5
# Bug was: while loop with counter starting at 1 skipped first element
# Fix: Used for loop to iterate through all elements
