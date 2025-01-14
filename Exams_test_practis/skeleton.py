# Входни данни
minutes_control = int(input())  # Минути на контролата
seconds_control = int(input())  # Секунди на контролата
length = float(input())  # Дължина на улея в метри
seconds_per_100m = int(input())  # Секунди за изминаване на 100 метра

# Изчисляване на контролното време в секунди
control_time_seconds = minutes_control * 60 + seconds_control

# Изчисляване на времето на Марин за преминаване на целия улей
marin_time = (length / 100) * seconds_per_100m

# Изчисляване на намалението на времето за всеки 120 метра
reduction_count = length // 120  # Колко пъти се прилага намалението
time_reduction = reduction_count * 2.5  # Общо намаление

# Крайното време на Марин след намалението
final_time = marin_time - time_reduction

# Проверка дали Марин печели квота
if final_time <= control_time_seconds:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {final_time:.3f}.")
else:
    difference = final_time - control_time_seconds
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
