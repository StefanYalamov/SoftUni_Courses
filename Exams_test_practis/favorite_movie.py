# Инициализация на променливите
best_movie = ""
best_movie_score = float('-inf')  # Започваме с минимално възможната стойност
movie_count = 0

# Четене на заглавията на филмите
while movie_count < 7:
    movie_title = input()

    if movie_title == "STOP":
        break

    # Увеличаваме броя на филмите
    movie_count += 1

    # Изчисляване на ASCII стойността на текущото заглавие
    movie_score = 0
    movie_length = len(movie_title)

    for char in movie_title:
        ascii_value = ord(char)
        if 'a' <= char <= 'z':  # Малка буква
            movie_score += ascii_value - 2 * movie_length
        elif 'A' <= char <= 'Z':  # Главна буква
            movie_score += ascii_value - movie_length
        else:  # Други символи (ако има такива)
            movie_score += ascii_value

    # Проверка дали това е най-добрият филм досега
    if movie_score > best_movie_score:
        best_movie = movie_title
        best_movie_score = movie_score

# Печатане на резултатите
if movie_count == 7:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {best_movie_score} ASCII sum.")
