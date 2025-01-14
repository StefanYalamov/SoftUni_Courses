# Входни данни
budget = float(input())
destination = input()
season = input()
days_count = int(input())

# Цени за дестинации и сезони
prices = {
    "Dubai": {"Summer": 40000, "Winter": 45000},
    "Sofia": {"Summer": 12500, "Winter": 17000},
    "London": {"Summer": 20250, "Winter": 24000}
}

# Отстъпки/надбавки за дестинациите
discounts = {
    "Dubai": 0.70,  # 30% отстъпка
    "Sofia": 1.25,  # 25% надбавка
    "London": 1.00  # няма промяна
}

# Изчисляване на общата цена
price_per_day = prices[destination][season]
total_price = price_per_day * days_count * discounts[destination]

# Проверка дали бюджетът е достатъчен
if budget >= total_price:
    remaining_budget = budget - total_price
    print(f"The budget for the movie is enough! We have {remaining_budget:.2f} leva left!")
else:
    needed_money = total_price - budget
    print(f"The director needs {needed_money:.2f} leva more!")
