# Четем контролната стойност
M = int(input())

# Списък за всички валидни комбинации
valid_combinations = []

# Обхождаме всички възможни стойности за a, b, c и d (в интервала [1, 9])
for a in range(1, 10):
    for b in range(1, 10):
        if a < b:  # Условието за a < b
            for c in range(1, 10):
                for d in range(1, 10):
                    if c > d:  # Условието за c > d
                        # Проверяваме дали произведението отговаря на M
                        if a * b + c * d == M:
                            # Добавяме валидната комбинация в списъка
                            valid_combinations.append(f"{a}{b}{c}{d}")

# Ако има валидни комбинации, ги отпечатваме
if valid_combinations:
    # Отпечатваме всички комбинации
    print(" ".join(valid_combinations))

    # Ако има поне четири комбинации, отпечатваме четвъртата като парола
    if len(valid_combinations) >= 4:
        print(f"Password: {valid_combinations[3]}")
    else:
        print("No!")
else:
    print("No!")
