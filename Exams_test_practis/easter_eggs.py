# Входни данни
number_of_eggs = int(input())  # Броят на боядисаните яйца

# Инициализация на броя яйца за всеки цвят
eggs_count = {
    "red": 0,
    "orange": 0,
    "blue": 0,
    "green": 0
}

# Четене на цветовете и преброяване на яйцата
for _ in range(number_of_eggs):
    color = input()  # Прочитаме цвета на яйцето
    if color in eggs_count:
        eggs_count[color] += 1  # Увеличаваме броя на яйцата за съответния цвят

# Изчисляване на максималния брой и съответния цвят
max_color = max(eggs_count, key=eggs_count.get)
max_count = eggs_count[max_color]

# Изход
print(f"Red eggs: {eggs_count['red']}")
print(f"Orange eggs: {eggs_count['orange']}")
print(f"Blue eggs: {eggs_count['blue']}")
print(f"Green eggs: {eggs_count['green']}")
print(f"Max eggs: {max_count} -> {max_color}")
