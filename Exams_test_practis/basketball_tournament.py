# Променливи за следене на броя на мачовете, победите и загубите
total_games = 0
total_wins = 0
total_losses = 0

# Четене на имената на турнирите, докато не получим "End of tournaments"
while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break

    # Брой мачове за текущия турнир
    number_of_games = int(input())

    # Обработка на всеки мач в турнира
    for game_number in range(1, number_of_games + 1):
        desi_points = int(input())  # Точки на отбора на Деси
        opponent_points = int(input())  # Точки на противниковия отбор

        # Увеличаваме броя на изиграните мачове
        total_games += 1

        # Определяне на резултата и отпечатване на съобщението
        if desi_points > opponent_points:
            win_difference = desi_points - opponent_points
            total_wins += 1
            print(f"Game {game_number} of tournament {tournament_name}: win with {win_difference} points.")
        else:
            loss_difference = opponent_points - desi_points
            total_losses += 1
            print(f"Game {game_number} of tournament {tournament_name}: lost with {loss_difference} points.")

# Изчисляване на процентите за победи и загуби
win_percentage = (total_wins / total_games) * 100
loss_percentage = (total_losses / total_games) * 100

# Отпечатване на крайния резултат
print(f"{win_percentage:.2f}% matches win")
print(f"{loss_percentage:.2f}% matches lost")
