# Въвеждане на капацитета на стадиона и общия брой фенове
stadium_capacity = int(input())  # Капацитет на стадиона
total_fans = int(input())  # Брой на всички фенове

# Променливи за броене на феновете в различните сектори
count_A = 0
count_B = 0
count_V = 0
count_G = 0

# Обхождане на всеки фен и събиране на броя им според сектора
for _ in range(total_fans):
    sector = input()  # Секторът на текущия фен
    if sector == "A":
        count_A += 1
    elif sector == "B":
        count_B += 1
    elif sector == "V":
        count_V += 1
    elif sector == "G":
        count_G += 1

# Изчисляване на процентите за всеки сектор спрямо общия брой фенове
percent_A = (count_A / total_fans) * 100
percent_B = (count_B / total_fans) * 100
percent_V = (count_V / total_fans) * 100
percent_G = (count_G / total_fans) * 100

# Изчисляване на общия процент на феновете спрямо капацитета на стадиона
total_fan_percentage = (total_fans / stadium_capacity) * 100

# Принтиране на резултатите, форматирани до втория знак след десетичната запетая
print(f"{percent_A:.2f}%")
print(f"{percent_B:.2f}%")
print(f"{percent_V:.2f}%")
print(f"{percent_G:.2f}%")
print(f"{total_fan_percentage:.2f}%")
