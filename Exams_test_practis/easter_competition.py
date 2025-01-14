# Четем броя на козунаците
number_of_cakes = int(input())

# Инициализиране на променливи за следене на най-добрия пекар
best_baker_name = ""
highest_score = 0

# Обработка на данни за всеки пекар
for _ in range(number_of_cakes):
    baker_name = input()
    current_score = 0

    # Четем оценките за текущия пекар
    while True:
        command = input()
        if command == "Stop":
            break
        # Добавяме оценката към текущия сбор точки на пекаря
        current_score += int(command)

    # Отпечатване на резултата за текущия пекар
    print(f"{baker_name} has {current_score} points.")

    # Проверка дали този пекар е с най-много точки досега
    if current_score > highest_score:
        highest_score = current_score
        best_baker_name = baker_name
        print(f"{baker_name} is the new number 1!")

# Отпечатваме крайния победител
print(f"{best_baker_name} won competition with {highest_score} points!")
