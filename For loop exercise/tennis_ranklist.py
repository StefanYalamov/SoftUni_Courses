WIN_POINTS = 2000
SEMI_FINAL_PINTS = 720
FINAL_POINTS = 1200

number_tournaments = int(input())
current_points = int(input())

total_points = 0
number_wins = 0

for _ in range(number_tournaments):
    stage = input()

    if stage == "W":
        total_points += WIN_POINTS
        number_wins += 1
    elif stage == "SF":
        total_points += SEMI_FINAL_PINTS
    elif stage == "F":
        total_points += FINAL_POINTS

print(f"Final points: {current_points + total_points}")
print(f"Average points: {total_points // number_tournaments}")
print(f"{number_wins / number_tournaments * 100:.2f}%")

# След подобрение стана така:

# Константи за точките
WIN_POINTS = 2000
SEMI_FINAL_POINTS = 720  # Поправено име
FINAL_POINTS = 1200

# Прочитане на входни данни
number_tournaments = int(input())  # Брой турнири
current_points = int(input())  # Начални точки

# Инициализиране на броячите
number_wins = 0

# Обработка на всеки турнир
for _ in range(number_tournaments):
    stage = input()

    if stage == "W":
        current_points += WIN_POINTS
        number_wins += 1
    elif stage == "SF":
        current_points += SEMI_FINAL_POINTS
    elif stage == "F":
        current_points += FINAL_POINTS

# Отпечатване на резултатите
print(f"Final points: {current_points}")
print(f"Average points: {current_points // number_tournaments}")
print(f"{number_wins / number_tournaments * 100:.2f}%")

