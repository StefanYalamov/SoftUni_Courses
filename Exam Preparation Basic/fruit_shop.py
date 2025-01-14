# Входни данни
price_strawberries = float(input())  # Цена на ягодите за килограм
bananas_kg = float(input())  # Количество на бананите в кг
oranges_kg = float(input())  # Количество на портокалите в кг
raspberries_kg = float(input())  # Количество на малините в кг
strawberries_kg = float(input())  # Количество на ягодите в кг

# Изчисляване на цените на останалите продукти
price_raspberries = price_strawberries / 2
price_oranges = price_raspberries - (0.4 * price_raspberries)
price_bananas = price_raspberries - (0.8 * price_raspberries)

# Изчисляване на общата сума за всеки продукт
total_raspberries = raspberries_kg * price_raspberries
total_oranges = oranges_kg * price_oranges
total_bananas = bananas_kg * price_bananas
total_strawberries = strawberries_kg * price_strawberries

# Обща сума
total_cost = total_raspberries + total_oranges + total_bananas + total_strawberries

# Извеждане на резултата форматиран до втората цифра след десетичната запетая
print(f"{total_cost:.2f}")
