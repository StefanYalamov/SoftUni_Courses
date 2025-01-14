# Четене на входните данни
budget = float(input())
number_of_series = int(input())

# Сумиране на всички цени на сериалите
total_price = 0

# Проверка за всеки сериал
for _ in range(number_of_series):
    series_name = input()
    series_price = float(input())

    # Проверка за прилагане на отстъпка
    if series_name == "Thrones":
        series_price *= 0.50  # 50% отстъпка
    elif series_name == "Lucifer":
        series_price *= 0.60  # 40% отстъпка
    elif series_name == "Protector":
        series_price *= 0.70  # 30% отстъпка
    elif series_name == "TotalDrama":
        series_price *= 0.80  # 20% отстъпка
    elif series_name == "Area":
        series_price *= 0.90  # 10% отстъпка

    # Добавяне на цената на текущия сериал към общата цена
    total_price += series_price

# Проверка дали бюджетът е достатъчен
if total_price <= budget:
    # Ако бюджетът е достатъчен, изчисляваме колко пари остават
    remaining_budget = budget - total_price
    print(f"You bought all the series and left with {remaining_budget:.2f} lv.")
else:
    # Ако бюджетът не е достатъчен, изчисляваме колко пари не достигат
    needed_money = total_price - budget
    print(f"You need {needed_money:.2f} lv. more to buy the series!")
