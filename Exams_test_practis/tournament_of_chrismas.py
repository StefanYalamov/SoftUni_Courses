# Четене на броя дни от конзолата
number_of_days = int(input())

# Инициализация на променливите за обща сума и броя на дните с победи
total_money = 0
days_with_wins = 0

# Итерация през всеки ден
for day in range(number_of_days):
    # Инициализация на дневните печалби и броя на победите и загубите за деня
    day_wins = 0
    day_loses = 0
    day_money = 0

    # Четене на игрите и резултатите за текущия ден
    while True:
        game = input()
        if game == "Finish":
            break
        result = input()

        if result == "win":
            day_money += 20
            day_wins += 1
        elif result == "lose":
            day_loses += 1

    # Ако има повече победи за деня, увеличаваме дневната сума с 10%
    if day_wins > day_loses:
        day_money *= 1.10
        days_with_wins += 1

    # Добавяне на дневната сума към общата
    total_money += day_money

# Проверка дали сме спечелили турнира
if days_with_wins > number_of_days / 2:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
