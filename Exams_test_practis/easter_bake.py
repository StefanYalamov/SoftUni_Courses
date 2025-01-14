import math

# Въвеждане на броя на козунаците
num_kozunaci = int(input())

# Инициализиране на променливи
total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0

# Обработване на данните за всеки козунак
for _ in range(num_kozunaci):
    sugar = int(input())  # Количество изразходвана захар
    flour = int(input())  # Количество изразходвано брашно

    # Намиране на общото количество захар и брашно
    total_sugar += sugar
    total_flour += flour

    # Проверка за максимално количество захар и брашно
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

# Изчисляване на броя нужни пакети захар и брашно
packets_sugar = math.ceil(total_sugar / 950)
packets_flour = math.ceil(total_flour / 750)

# Отпечатване на резултатите
print(f"Sugar: {packets_sugar}")
print(f"Flour: {packets_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
