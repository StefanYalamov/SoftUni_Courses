# Входни данни
budget = float(input())
nights = int(input())
price_per_night = float(input())
extra_expenses_percent = int(input())

# Проверка за отстъпка при повече от 7 нощувки
if nights > 7:
    price_per_night *= 0.95

# Изчисляване на общите разходи
total_night_cost = nights * price_per_night
extra_expenses = (extra_expenses_percent / 100) * budget
total_cost = total_night_cost + extra_expenses

# Проверка дали бюджетът е достатъчен
if total_cost <= budget:
    money_left = budget - total_cost
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    money_needed = total_cost - budget
    print(f"{money_needed:.2f} leva needed.")
