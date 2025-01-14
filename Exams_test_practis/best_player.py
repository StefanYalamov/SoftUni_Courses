# Инициализация на променливите
best_player = ""
max_goals = 0

# Четем входа, докато не получим "END"
while True:
    player = input()  # Четем името на играча
    if player == "END":
        break  # Прекратяваме, ако командата е "END"

    goals = int(input())  # Четем броя голове
    # Ако този играч има повече голове от текущия максимален
    if goals > max_goals:
        best_player = player
        max_goals = goals

    # Прекратяваме, ако играчът има 10 или повече гола
    if goals >= 10:
        break

# Извеждаме резултатите
print(f"{best_player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
