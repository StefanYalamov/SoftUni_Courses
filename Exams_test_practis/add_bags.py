# Константи за изчисление на процентите
UNDER_10KG_MULTIPLIER = 0.20
BETWEEN_10_20KG_MULTIPLIER = 0.50

# Въвеждане на входните данни
price_over_20kg = float(input())  # Цена на багаж над 20 кг
weight_bag = float(input())       # Тегло на багаж
days_to_trip = int(input())       # Дни до пътуването
number_of_bags = int(input())     # Брой багажи

# Определяне на базовата цена на багажа според теглото
if weight_bag < 10:
    base_price = price_over_20kg * UNDER_10KG_MULTIPLIER
elif 10 <= weight_bag <= 20:
    base_price = price_over_20kg * BETWEEN_10_20KG_MULTIPLIER
else:
    base_price = price_over_20kg

# Определяне на процента на оскъпяване според дните до пътуването
if days_to_trip > 30:
    base_price *= 1.10  # Оскъпяване с 10%
elif 7 <= days_to_trip <= 30:
    base_price *= 1.15  # Оскъпяване с 15%
else:
    base_price *= 1.40  # Оскъпяване с 40%

# Изчисляване на крайната сума за всички багажи
total_price = base_price * number_of_bags

# Отпечатване на резултата
print(f"The total price of bags is: {total_price:.2f} lv.")
