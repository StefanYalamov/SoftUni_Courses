# Вход: Брой дни и брой часове за всеки ден
days = int(input())
hours = int(input())

# Инициализация на променлива за общата сума за всички дни
total_sum = 0

# Променлива за текущия ден
current_day = 1

# Обхождаме дните, използвайки while цикъл
while current_day <= days:
    day_sum = 0  # Сума за текущия ден
    current_hour = 1  # Брояч за часовете

    # Вложен while цикъл за часовете
    while current_hour <= hours:
        if current_day % 2 == 0 and current_hour % 2 != 0:
            # Четен ден и нечетен час - 2.50 лева
            day_sum += 2.50
        elif current_day % 2 != 0 and current_hour % 2 == 0:
            # Нечетен ден и четен час - 1.25 лева
            day_sum += 1.25
        else:
            # Всички останали случаи - 1 лев
            day_sum += 1

        current_hour += 1  # Преминаваме към следващия час

    # Отпечатваме резултата за текущия ден
    print(f"Day: {current_day} - {day_sum:.2f} leva")

    # Добавяме дневната сума към общата сума
    total_sum += day_sum

    # Преминаваме към следващия ден
    current_day += 1

# Отпечатваме общата сума за всички дни
print(f"Total: {total_sum:.2f} leva")
