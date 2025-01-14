# Входни данни
budget = float(input())               # Бюджет за филма
destination = input()                 # Дестинация: "Dubai", "Sofia", "London"
season = input()                      # Сезон: "Summer" или "Winter"
days_count = int(input())             # Брой снимачни дни

# Цени за един снимачен ден според дестинация и сезон
price_per_day = 0

# Определяне на цената на ден според дестинацията и сезона
if destination == "Dubai":
    if season == "Summer":
        price_per_day = 40000
    elif season == "Winter":
        price_per_day = 45000
elif destination == "Sofia":
    if season == "Summer":
        price_per_day = 12500
    elif season == "Winter":
        price_per_day = 17000
elif destination == "London":
    if season == "Summer":
        price_per_day = 20250
    elif season == "Winter":
        price_per_day = 24000

# Изчисляване на общата цена за всички дни
total_price = price_per_day * days_count

# Прилагане на данъчни облекчения/облагания
if destination == "Dubai":
    total_price *= 0.70  # 30% отстъпка
elif destination == "Sofia":
    total_price *= 1.25  # 25% оскъпяване

# Проверка дали бюджетът е достатъчен
if budget >= total_price:
    remaining_budget = budget - total_price
    print(f"The budget for the movie is enough! We have {remaining_budget:.2f} leva left!")
else:
    needed_money = total_price - budget
    print(f"The director needs {needed_money:.2f} leva more!")
