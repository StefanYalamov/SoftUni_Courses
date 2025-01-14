# Прочитане на входните данни
budget = float(input())  # Бюджет за филма
number_of_extras = int(input())  # Брой статисти
clothes_price_per_extra = float(input())  # Цена на облекло за един статист

# Изчисляване на цената за декора
decor_cost = budget * 0.10

# Изчисляване на общата цена за облекло
total_clothes_cost = number_of_extras * clothes_price_per_extra

# Ако броят на статистите е повече от 150, получават 10% отстъпка
if number_of_extras > 150:
    total_clothes_cost *= 0.90

# Изчисляване на общите разходи
total_cost = decor_cost + total_clothes_cost

# Проверка дали бюджетът е достатъчен
if total_cost <= budget:
    remaining_money = budget - total_cost
    print("Action!")
    print(f"Wingard starts filming with {remaining_money:.2f} leva left.")
else:
    money_needed = total_cost - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
