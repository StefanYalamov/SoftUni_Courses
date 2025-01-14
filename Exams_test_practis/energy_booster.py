# Стъпка 1: Прочитане на входните данни
fruit = input()
set_size = input()
number_of_sets = int(input())

# Стъпка 2: Определяне на цените в зависимост от плодовете и размера
# Цени за "small" комплект (2 бр.)
prices_small = {
    "Watermelon": 56.00,
    "Mango": 36.66,
    "Pineapple": 42.10,
    "Raspberry": 20.00
}

# Цени за "big" комплект (5 бр.)
prices_big = {
    "Watermelon": 28.70,
    "Mango": 19.60,
    "Pineapple": 24.80,
    "Raspberry": 15.20
}

# Стъпка 3: Изчисление на цената на един комплект в зависимост от размера
if set_size == "small":
    price_per_set = prices_small[fruit] * 2  # Цената на малък комплект (2 бр.)
else:  # set_size == "big"
    price_per_set = prices_big[fruit] * 5  # Цената на голям комплект (5 бр.)

# Стъпка 4: Изчисление на общата сума за всички поръчани комплекти
total_price = price_per_set * number_of_sets

# Стъпка 5: Прилагане на отстъпки, ако е необходимо
if 400 <= total_price <= 1000:
    total_price -= total_price * 0.15  # 15% отстъпка
elif total_price > 1000:
    total_price -= total_price * 0.50  # 50% отстъпка

# Стъпка 6: Извеждане на крайния резултат, форматиран до втората цифра след десетичната запетая
print(f"{total_price:.2f} lv.")
