# Четене на входни данни
movie_name = input()        # Име на филма ("John Wick", "Star Wars", "Jumanji")
package = input()           # Избран пакет ("Drink", "Popcorn", "Menu")
tickets_count = int(input())  # Брой закупени билети

# Определяне на цената на билет според филма и пакета
price_per_ticket = 0
if movie_name == "John Wick":
    if package == "Drink":
        price_per_ticket = 12
    elif package == "Popcorn":
        price_per_ticket = 15
    elif package == "Menu":
        price_per_ticket = 19
elif movie_name == "Star Wars":
    if package == "Drink":
        price_per_ticket = 18
    elif package == "Popcorn":
        price_per_ticket = 25
    elif package == "Menu":
        price_per_ticket = 30
elif movie_name == "Jumanji":
    if package == "Drink":
        price_per_ticket = 9
    elif package == "Popcorn":
        price_per_ticket = 11
    elif package == "Menu":
        price_per_ticket = 14

# Изчисляване на общата цена
total_price = price_per_ticket * tickets_count

# Прилагане на отстъпки
if movie_name == "Star Wars" and tickets_count >= 4:
    total_price *= 0.70  # Отстъпка от 30% (100% - 30%)
elif movie_name == "Jumanji" and tickets_count == 2:
    total_price *= 0.85  # Отстъпка от 15% (100% - 15%)

# Отпечатване на резултата, форматиран до втората цифра след десетичната запетая
print(f"Your bill is {total_price:.2f} leva.")
