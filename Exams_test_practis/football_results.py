# Входни данни
match1 = input()  # Резултат от първия мач
match2 = input()  # Резултат от втория мач
match3 = input()  # Резултат от третия мач

# Променливи за броене на победи, загуби и равенства
wins = 0
losses = 0
draws = 0

# Проверка на всеки мач
for match in [match1, match2, match3]:
    # Разделяме резултата във формат "X:Y"
    our_goals = int(match[0])  # Първата цифра е головете на нашия отбор
    opponent_goals = int(match[2])  # Третата цифра е головете на противника

    # Определяме резултата на мача
    if our_goals > opponent_goals:
        wins += 1
    elif our_goals < opponent_goals:
        losses += 1
    else:
        draws += 1

# Отпечатване на резултата
print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")
