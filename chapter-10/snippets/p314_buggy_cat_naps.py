def nap_time(hours_list):
    total = 0
    counter = 1
    while counter < len(hours_list):
            total += hours_list[counter]
            counter += 1
    return total
cat_naps = [2, 3, 1.5, 4]
print("Total nap time:", nap_time(cat_naps))
