def nap_time(hours_list):
    total = 0
    for nap in hours_list:
        total += nap
    return total

cat_naps = [2, 3, 1.5, 4]
print("Total nap time:", nap_time(cat_naps))