# Прочитане на входните данни
total_visitors = int(input())  # Броят на посетителите

# Инициализиране на броячите за всяка дейност
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

# Променливи за броя трениращи и купуващи продукти
work_out_count = 0
protein_count = 0

# Обработка на всеки посетител
for _ in range(total_visitors):
    activity = input()  # Дейност на посетителя

    # Проверка на дейността и увеличаване на съответния брояч
    if activity == "Back":
        back += 1
        work_out_count += 1
    elif activity == "Chest":
        chest += 1
        work_out_count += 1
    elif activity == "Legs":
        legs += 1
        work_out_count += 1
    elif activity == "Abs":
        abs += 1
        work_out_count += 1
    elif activity == "Protein shake":
        protein_shake += 1
        protein_count += 1
    elif activity == "Protein bar":
        protein_bar += 1
        protein_count += 1

# Изчисляване на процентите
work_out_percentage = (work_out_count / total_visitors) * 100
protein_percentage = (protein_count / total_visitors) * 100

# Отпечатване на резултатите
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{work_out_percentage:.2f}% - work out")
print(f"{protein_percentage:.2f}% - protein")
