# Стъпка 1: Прочитане на входните данни
initial_sum = float(input())  # Наличната сума
gender = input()              # Пол ('m' за мъж, 'f' за жена)
age = int(input())            # Възраст на клиента
sport = input()               # Спорт

# Стъпка 2: Определяне на цените за различните спортове в зависимост от пола
price_male = {
    "Gym": 42.00,
    "Boxing": 41.00,
    "Yoga": 45.00,
    "Zumba": 34.00,
    "Dances": 51.00,
    "Pilates": 39.00
}

price_female = {
    "Gym": 35.00,
    "Boxing": 37.00,
    "Yoga": 42.00,
    "Zumba": 31.00,
    "Dances": 53.00,
    "Pilates": 37.00
}

# Стъпка 3: Избиране на подходящия речник за цени в зависимост от пола
if gender == 'm':
    base_price = price_male[sport]
else:
    base_price = price_female[sport]

# Стъпка 4: Проверка за ученическа отстъпка
if age <= 19:
    base_price *= 0.80  # Прилагане на 20% отстъпка

# Стъпка 5: Сравнение на крайната цена с наличната сума
if initial_sum >= base_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    needed_money = base_price - initial_sum
    print(f"You don't have enough money! You need ${needed_money:.2f} more.")
