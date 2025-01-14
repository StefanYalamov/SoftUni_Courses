# Прочитане на името на играча
player_name = input()

# Инициализиране на началните точки и броячите
current_points = 301
successful_shots = 0
unsuccessful_shots = 0

# Стартиране на основния while цикъл
while current_points > 0:
    command = input()  # Прочитане на поле или команда "Retire"

    if command == "Retire":
        # Играчът се отказва от играта
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    # Прочитане на точките за съответното поле
    field_type = command
    points = int(input())

    # Изчисляване на точките според полето
    if field_type == "Single":
        score = points
    elif field_type == "Double":
        score = points * 2
    elif field_type == "Triple":
        score = points * 3

    # Проверка дали изстрелът е успешен
    if score <= current_points:
        # Успешен изстрел - изваждаме точките
        current_points -= score
        successful_shots += 1
    else:
        # Неуспешен изстрел - точките са повече от наличните
        unsuccessful_shots += 1

# Проверка за победа - останалите точки са 0
if current_points == 0:
    print(f"{player_name} won the leg with {successful_shots} shots.")
