##Given 3 list
list_1 = [10, 20, 40, 60]
list_2 = [20, 25, 35, 40]
list_3 = [30, 35, 40, 45]

result = []

combined_list = list_1 + list_2 + list_3


seen = set()
duplicates = set()


for data in combined_list:
    if data in seen:
        duplicates.add(data)
    else:
        seen.add(data)

result = list(duplicates)

print("Duplicates across the lists:", result)
