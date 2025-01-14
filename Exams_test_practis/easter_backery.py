# Константи за процентите, спрямо цената на брашното
SUGAR_DISCOUNT = 0.75  # Цената на захарта е 25% по-ниска от цената на брашното
EGGS_MARKUP = 1.10     # Цената на яйцата е 10% по-висока от цената на брашното
YEAST_DISCOUNT = 0.20  # Цената на маята е 80% по-ниска от цената на захарта

# Входни данни
price_flour_per_kg = float(input())  # Цена на брашното за един килограм
kg_flour = float(input())  # Килограми на брашното
kg_sugar = float(input())  # Килограми на захарта
number_of_egg_cartons = int(input())  # Брой кори с яйца
number_of_yeast_packs = int(input())  # Пакети мая

# Изчисляване на цените за останалите продукти
price_sugar_per_kg = price_flour_per_kg * SUGAR_DISCOUNT
price_egg_carton = price_flour_per_kg * EGGS_MARKUP
price_yeast_pack = price_sugar_per_kg * YEAST_DISCOUNT

# Изчисляване на общите разходи
total_flour_cost = kg_flour * price_flour_per_kg
total_sugar_cost = kg_sugar * price_sugar_per_kg
total_egg_cost = number_of_egg_cartons * price_egg_carton
total_yeast_cost = number_of_yeast_packs * price_yeast_pack

# Обща сума за всички продукти
total_cost = total_flour_cost + total_sugar_cost + total_egg_cost + total_yeast_cost

# Отпечатване на резултата с форматиране до втората цифра след десетичната запетая
print(f"{total_cost:.2f}")
