import math

# Входни данни
record_seconds = float(input())  # Рекордът в секунди
distance_meters = float(input())  # Разстоянието в метри
time_per_meter = float(input())  # Времето за 1 метър

# Изчисляване на времето за изкачване без забавяния
total_time = distance_meters * time_per_meter

# Изчисляване на допълнителното време заради наклона
additional_time = math.floor(distance_meters / 50) * 30

# Общо време с добавени забавяния
total_time += additional_time

# Проверка дали Георги е подобрил рекорда
if total_time < record_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {total_time - record_seconds:.2f} seconds slower.")
