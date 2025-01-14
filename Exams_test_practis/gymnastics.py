# Входни данни
country = input()  # Държава
device = input()  # Уред

# Инициализация на оценките за трудност и изпълнение
difficulty_score = 0.0
execution_score = 0.0

# Проверка на оценките според държавата и уреда
if country == "Russia":
    if device == "ribbon":
        difficulty_score = 9.100
        execution_score = 9.400
    elif device == "hoop":
        difficulty_score = 9.300
        execution_score = 9.800
    elif device == "rope":
        difficulty_score = 9.600
        execution_score = 9.000
elif country == "Bulgaria":
    if device == "ribbon":
        difficulty_score = 9.600
        execution_score = 9.400
    elif device == "hoop":
        difficulty_score = 9.550
        execution_score = 9.750
    elif device == "rope":
        difficulty_score = 9.500
        execution_score = 9.400
elif country == "Italy":
    if device == "ribbon":
        difficulty_score = 9.200
        execution_score = 9.500
    elif device == "hoop":
        difficulty_score = 9.450
        execution_score = 9.350
    elif device == "rope":
        difficulty_score = 9.700
        execution_score = 9.150

# Изчисляване на общата оценка
total_score = difficulty_score + execution_score

# Изчисляване на процента, който не им достига до максималните 20 точки
percent_missing = (20 - total_score) / 20 * 100

# Изход
print(f"The team of {country} get {total_score:.3f} on {device}.")
print(f"{percent_missing:.2f}%")


# Вариант с Фор цикъл :


# Държави и уреди
countries = ["Russia", "Bulgaria", "Italy"]
devices = ["ribbon", "hoop", "rope"]

# Оценки за трудност и изпълнение, подредени според страните и уредите
difficulty_scores = [
    [9.100, 9.300, 9.600],  # Russia
    [9.600, 9.550, 9.500],  # Bulgaria
    [9.200, 9.450, 9.700]   # Italy
]

execution_scores = [
    [9.400, 9.800, 9.000],  # Russia
    [9.400, 9.750, 9.400],  # Bulgaria
    [9.500, 9.350, 9.150]   # Italy
]

# Входни данни
country = input()  # Държава
device = input()  # Уред

# Намиране на индекса на държавата и уреда с помощта на for цикъл
for i in range(len(countries)):
    if countries[i] == country:
        country_index = i
        break

for j in range(len(devices)):
    if devices[j] == device:
        device_index = j
        break

# Изчисляване на общата оценка
total_score = difficulty_scores[country_index][device_index] + execution_scores[country_index][device_index]

# Изчисляване на процента, който не им достига до максималните 20 точки
percent_missing = (20 - total_score) / 20 * 100

# Изход
print(f"The team of {country} get {total_score:.3f} on {device}.")
print(f"{percent_missing:.2f}%")
