# Входни данни
movie_name = input()
days = int(input())
tickets_per_day = int(input())
ticket_price = float(input())
cinema_percentage = int(input())

# Изчисляване на общия приход от филма
total_revenue_per_day = tickets_per_day * ticket_price
total_revenue = total_revenue_per_day * days

# Изчисляване на процента, който остава за киното
cinema_profit = total_revenue * (cinema_percentage / 100)

# Изчисляване на приходите за студиото
studio_profit = total_revenue - cinema_profit

# Форматиране на изхода и отпечатване на резултата
print(f"The profit from the movie {movie_name} is {studio_profit:.2f} lv.")
