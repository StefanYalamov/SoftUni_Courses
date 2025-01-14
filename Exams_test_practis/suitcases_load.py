# Четене на капацитета на багажника
capacity = float(input())

# Инициализация на брояч и оставащ капацитет
suitcase_count = 0
remaining_capacity = capacity

# Четене на командите или обема на куфарите
while True:
    command = input()

    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    # Конвертиране на входа в реално число (обем на куфар)
    suitcase_volume = float(command)

    # Проверка дали куфарът е третият (всеки трети куфар се увеличава с 10%)
    if (suitcase_count + 1) % 3 == 0:
        suitcase_volume *= 1.10

    # Проверка дали оставащият капацитет е достатъчен
    if suitcase_volume > remaining_capacity:
        print("No more space!")
        break

    # Ако куфарът се побира, го добавяме и намаляваме оставащото място
    remaining_capacity -= suitcase_volume
    suitcase_count += 1

# Извеждане на статистика
print(f"Statistic: {suitcase_count} suitcases loaded.")
