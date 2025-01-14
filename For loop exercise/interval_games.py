# Въвеждане на броя на ходовете
num_moves = int(input())

# Инициализация на променливите
total_score = 0  # Начален резултат
count_0_9 = 0
count_10_19 = 0
count_20_29 = 0
count_30_39 = 0
count_40_50 = 0
invalid_numbers = 0

# Обхождаме всеки ход
for _ in range(num_moves):
    number = int(input())  # Въвеждаме числото за текущия ход

    # Проверка в кой интервал попада числото и съответно изчисляване на точки
    if 0 <= number <= 9:
        total_score += number * 0.20
        count_0_9 += 1
    elif 10 <= number <= 19:
        total_score += number * 0.30
        count_10_19 += 1
    elif 20 <= number <= 29:
        total_score += number * 0.40
        count_20_29 += 1
    elif 30 <= number <= 39:
        total_score += 50
        count_30_39 += 1
    elif 40 <= number <= 50:
        total_score += 100
        count_40_50 += 1
    else:
        total_score /= 2  # Невалидно число – делим резултата на 2
        invalid_numbers += 1

# Изчисляване на процентите за всеки интервал спрямо общия брой ходове
percent_0_9 = (count_0_9 / num_moves) * 100
percent_10_19 = (count_10_19 / num_moves) * 100
percent_20_29 = (count_20_29 / num_moves) * 100
percent_30_39 = (count_30_39 / num_moves) * 100
percent_40_50 = (count_40_50 / num_moves) * 100
percent_invalid = (invalid_numbers / num_moves) * 100

# Извеждане на резултатите
print(f"{total_score:.2f}")
print(f"From 0 to 9: {percent_0_9:.2f}%")
print(f"From 10 to 19: {percent_10_19:.2f}%")
print(f"From 20 to 29: {percent_20_29:.2f}%")
print(f"From 30 to 39: {percent_30_39:.2f}%")
print(f"From 40 to 50: {percent_40_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
