# Константи за добавяне на точки
POINTS_FOR_RED = 5
POINTS_FOR_ORANGE = 10
POINTS_FOR_YELLOW = 15
POINTS_FOR_WHITE = 20

# Прочитане на входните данни
number_of_balls = int(input())

# Променливи за съхраняване на резултатите
total_points = 0
red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
other_count = 0
black_divisions = 0

# Обработка на всеки въведен цвят на топка
for _ in range(number_of_balls):
    color = input().strip().lower()  # Четем и нормализираме текста

    if color == "red":
        total_points += POINTS_FOR_RED
        red_count += 1
    elif color == "orange":
        total_points += POINTS_FOR_ORANGE
        orange_count += 1
    elif color == "yellow":
        total_points += POINTS_FOR_YELLOW
        yellow_count += 1
    elif color == "white":
        total_points += POINTS_FOR_WHITE
        white_count += 1
    elif color == "black":
        total_points //= 2  # Разделяне на точките на две (цяло число)
        black_divisions += 1
    else:
        other_count += 1  # Ако цветът не съответства на горните, се добавя към другите цветове

# Отпечатване на резултатите
print(f"Total points: {total_points}")
print(f"Red balls: {red_count}")
print(f"Orange balls: {orange_count}")
print(f"Yellow balls: {yellow_count}")
print(f"White balls: {white_count}")
print(f"Other colors picked: {other_count}")
print(f"Divides from black balls: {black_divisions}")
