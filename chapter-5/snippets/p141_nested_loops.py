for i in range(1, 4):
    for j in range(1, 4):
        product = i * j
        print(f"{i} x {j} = {product}")
    print("---")


list_of_lists = [
    ["Wiesje", "Pino", "Hedgehog"],
    ["Zia", "Python", "Writing"],
    ["Muchu", "Napping"]
]

for inner_list in list_of_lists:
    for item in inner_list:
        print(item)