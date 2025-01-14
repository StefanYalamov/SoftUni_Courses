# Въвеждане на броя дни и общото количество храна
days = int(input())
total_food = float(input())

# Създаване на броячи за всички необходими стойности
total_eaten_food = 0  # Общо изядена храна от всички дни
total_biscuits = 0  # Общ брой бисквитки
dog_food = 0  # Общо изядена храна от кучето
cat_food = 0  # Общо изядена храна от котката

# Обработваме информацията за всеки ден
for day in range(1, days + 1):
    # Въвеждане на количеството изядена храна от кучето и котката
    dog_daily_food = int(input())  # Храна за кучето за деня
    cat_daily_food = int(input())  # Храна за котката за деня

    # Изчисляваме общата изядена храна за деня
    daily_total_food = dog_daily_food + cat_daily_food
    total_eaten_food += daily_total_food

    # Добавяме към брояча на храна за кучето и котката
    dog_food += dog_daily_food
    cat_food += cat_daily_food

    # Ако денят е всеки трети (награда с бисквитки)
    if day % 3 == 0:
        total_biscuits += daily_total_food * 0.10

# Изчисляваме процентите за всяка категория
percent_total_eaten = (total_eaten_food / total_food) * 100
percent_dog = (dog_food / total_eaten_food) * 100
percent_cat = (cat_food / total_eaten_food) * 100

# Отпечатване на резултатите
print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_total_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")
