# Прочитане на броя на филмите
number_of_movies = int(input())

# Инициализация на променливи
max_rating = -1  # Начална стойност за максималния рейтинг
min_rating = 11  # Начална стойност за минималния рейтинг (над максималната възможна)
total_rating = 0  # Обща сума на всички рейтинги
highest_rated_movie = ""  # Име на филма с най-висок рейтинг
lowest_rated_movie = ""  # Име на филма с най-нисък рейтинг

# Обхождане на всеки филм
for _ in range(number_of_movies):
    movie_name = input()  # Име на филма
    rating = float(input())  # Рейтинг на филма

    # Проверка за максимален рейтинг
    if rating > max_rating:
        max_rating = rating
        highest_rated_movie = movie_name

    # Проверка за минимален рейтинг
    if rating < min_rating:
        min_rating = rating
        lowest_rated_movie = movie_name

    # Добавяне на текущия рейтинг към общата сума
    total_rating += rating

# Изчисляване на средния рейтинг
average_rating = total_rating / number_of_movies

# Отпечатване на резултатите
print(f"{highest_rated_movie} is with highest rating: {max_rating:.1f}")
print(f"{lowest_rated_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
