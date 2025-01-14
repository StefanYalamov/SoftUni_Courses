# Въвеждане на броя на групите от конзолата
number_of_groups = int(input())

# Създаваме променливи за броя катерачи за всеки връх
musala_climbers = 0
montblanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

# Променлива за общия брой катерачи
total_climbers = 0

# Прочитане на броя на катерачите за всяка група
for _ in range(number_of_groups):
    group_size = int(input())  # Прочитане на броя на катерачите в текущата група
    total_climbers += group_size  # Добавяне на броя на катерачите към общия брой

    # Определяне на кой връх ще изкачват според броя им
    if group_size <= 5:
        musala_climbers += group_size
    elif group_size <= 12:
        montblanc_climbers += group_size
    elif group_size <= 25:
        kilimanjaro_climbers += group_size
    elif group_size <= 40:
        k2_climbers += group_size
    else:
        everest_climbers += group_size

# Изчисляване на процента катерачи за всеки връх
musala_percent = (musala_climbers / total_climbers) * 100
montblanc_percent = (montblanc_climbers / total_climbers) * 100
kilimanjaro_percent = (kilimanjaro_climbers / total_climbers) * 100
k2_percent = (k2_climbers / total_climbers) * 100
everest_percent = (everest_climbers / total_climbers) * 100

# Печат на резултатите
print(f"{musala_percent:.2f}%")
print(f"{montblanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
