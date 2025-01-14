# Прочитане на входните данни
number_of_tournaments = int(input())  # Брой турнири
starting_points = int(input())  # Начален брой точки

# Инициализиране на броячи и суми
total_points = starting_points
points_from_tournaments = 0
tournaments_won = 0

# Обработка на всеки турнир
for _ in range(number_of_tournaments):
    result = input()  # Резултат за текущия турнир

    if result == "W":
        points_from_tournaments += 2000
        tournaments_won += 1
    elif result == "F":
        points_from_tournaments += 1200
    elif result == "SF":
        points_from_tournaments += 720

# Общ брой точки
total_points += points_from_tournaments

# Изчисляване на средните точки и процент победи
average_points = points_from_tournaments // number_of_tournaments
win_percentage = (tournaments_won / number_of_tournaments) * 100

# Отпечатване на резултатите
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{win_percentage:.2f}%")
