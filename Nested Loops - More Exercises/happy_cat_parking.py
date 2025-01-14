# Прочитаме входа
days = int(input())
hours_per_day = int(input())

# Променлива за общата сума за всички дни
total_sum = 0

# Обхождаме дните
for day in range(1, days + 1):
    day_sum = 0  # Променлива за сумата за текущия ден

    # Обхождаме часовете за текущия ден
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            # Четен ден и нечетен час => таксата е 2.50 лв.
            day_sum += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            # Нечетен ден и четен час => таксата е 1.25 лв.
            day_sum += 1.25
        else:
            # Всички други случаи => таксата е 1.00 лв.
            day_sum += 1.00

    # Отпечатваме сумата за текущия ден
    print(f"Day: {day} - {day_sum:.2f} leva")

    # Добавяме сумата за деня към общата сума
    total_sum += day_sum

# Отпечатваме общата сума за всички дни
print(f"Total: {total_sum:.2f} leva")
