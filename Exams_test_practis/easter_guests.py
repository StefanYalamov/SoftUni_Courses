from math import ceil

# Константи
PRICE_PER_EASTER_BREAD = 4  # Цена на един козунак
PRICE_PER_EGG = 0.45        # Цена на едно яйце

# Входни данни
number_of_guests = int(input())  # Брой гости
budget = float(input())          # Бюджет на Любо

# Изчисляване на броя на козунаците и яйцата
easter_breads_needed = ceil(number_of_guests / 3)  # Закръгляне нагоре, тъй като един козунак стига за 3-ма
eggs_needed = number_of_guests * 2                 # Всеки гост получава по 2 яйца

# Изчисляване на разходите
total_cost_breads = easter_breads_needed * PRICE_PER_EASTER_BREAD
total_cost_eggs = eggs_needed * PRICE_PER_EGG
total_cost = total_cost_breads + total_cost_eggs

# Проверка дали бюджетът е достатъчен
if total_cost <= budget:
    money_left = budget - total_cost
    print(f"Lyubo bought {easter_breads_needed} Easter bread and {eggs_needed} eggs.")
    print(f"He has {money_left:.2f} lv. left.")
else:
    money_needed = total_cost - budget
    print("Lyubo doesn't have enough money.")
    print(f"He needs {money_needed:.2f} lv. more.")
