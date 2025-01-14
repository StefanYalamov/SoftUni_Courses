# Входни данни
days = int(input())
total_food = float(input())

# Инициализиране на променливи
total_eaten_food = 0
total_biscuits = 0
dog_food = 0
cat_food = 0

# Обработване на данните за всеки ден
for day in range(1, days + 1):
    dog_daily_food = int(input())
    cat_daily_food = int(input())

    # Общата храна за деня
    daily_total_food = dog_daily_food + cat_daily_food
    total_eaten_food += daily_total_food
    dog_food += dog_daily_food
    cat_food += cat_daily_food

    # На всеки 3-ти ден добавяме бисквити
    if day % 3 == 0:
        total_biscuits += daily_total_food * 0.10

# Изчисляване на процентите
percent_total_eaten = (total_eaten_food / total_food) * 100
percent_dog = (dog_food / total_eaten_food) * 100
percent_cat = (cat_food / total_eaten_food) * 100

# Извеждане на резултата
print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_total_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")
