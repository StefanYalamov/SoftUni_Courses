# Стъпка 1: Входни данни
minutes_per_walk = int(input())  # Минутите за всяка разходка
number_of_walks = int(input())   # Броят на разходките на ден
calories_intake = int(input())   # Приетите калории за деня

# Стъпка 2: Изчисление на общите изгорени калории
total_minutes = minutes_per_walk * number_of_walks
total_burned_calories = total_minutes * 5  # Изгорени калории

# Стъпка 3: Проверка дали изгорените калории са поне 50% от приетите калории
required_burned_calories = calories_intake / 2

# Стъпка 4: Извеждане на резултата
if total_burned_calories >= required_burned_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.")
