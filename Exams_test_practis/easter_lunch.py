# Ценови константи
PRICE_PER_COZUNAK = 3.20
PRICE_PER_CORA = 4.35
PRICE_PER_KILO_KURABII = 5.40
PRICE_PER_EGG_COLOR = 0.15

# Входни данни
number_of_cozunaks = int(input())  # Брой козунаци
number_of_egg_cartons = int(input())  # Брой кори с яйца
kilos_of_kurabii = int(input())  # Килограми курабии

# Изчисляване на разходите
price_cozunaks = number_of_cozunaks * PRICE_PER_COZUNAK
price_egg_cartons = number_of_egg_cartons * PRICE_PER_CORA
price_kurabii = kilos_of_kurabii * PRICE_PER_KILO_KURABII
price_for_egg_color = number_of_egg_cartons * 12 * PRICE_PER_EGG_COLOR

# Общо разходи
total_expense = price_cozunaks + price_egg_cartons + price_kurabii + price_for_egg_color

# Отпечатване на резултата
print(f"{total_expense:.2f}")
