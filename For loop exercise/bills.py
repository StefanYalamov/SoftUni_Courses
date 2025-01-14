# Въвеждане на броя месеци
months = int(input())

# Инициализация на променливи за общите разходи
total_electricity = 0  # Общи разходи за ток
total_water = months * 20  # Общи разходи за вода (всеки месец е фиксиран 20 лв.)
total_internet = months * 15  # Общи разходи за интернет (всеки месец е фиксиран 15 лв.)
total_other = 0  # Общи разходи за категория "Други"
total_expenses = 0  # Общи разходи за всички категории

# Обхождане на всеки месец
for _ in range(months):
    electricity = float(input())  # Въвеждане на разхода за ток за текущия месец
    total_electricity += electricity  # Добавяне към общите разходи за ток

    # Изчисляване на "Други" разходи за текущия месец
    monthly_total = electricity + 20 + 15  # Ток + Вода + Интернет
    other_expense = monthly_total * 1.20  # Добавяне на 20% от сумата
    total_other += other_expense  # Добавяне към общите разходи за "Други"

# Изчисляване на общите разходи
total_expenses = total_electricity + total_water + total_internet + total_other

# Изчисляване на средния разход на месец
average_expense = total_expenses / months

# Принтиране на резултатите, форматирани до втория знак след десетичната запетая
print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {average_expense:.2f} lv")
