# Прочитане на входа
number_of_floors = int(input())
rooms_per_floor = int(input())

# Обхождаме етажите от най-високия към най-ниския
for floor in range(number_of_floors, 0, -1):
    result = ""
    if floor == number_of_floors:
        prefix = "L"  # Последният етаж е с "L"
    elif floor % 2 == 0:
        prefix = "O"  # Четните етажи са офиси
    else:
        prefix = "A"  # Нечетните етажи са апартаменти

    for room_number in range(rooms_per_floor):
        result += f"{prefix}{floor}{room_number} "

    print(result.strip())  # Премахваме излишния интервал в края
