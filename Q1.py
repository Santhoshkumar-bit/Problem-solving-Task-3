list_1 = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = []
odd_numbers = []

for data in list_1:
    if data % 2 == 0:
        even_numbers.append(data)
    else:
        odd_numbers.append(data)

print("Even Number List : ", even_numbers)
print("Odd Number List : ", odd_numbers)
