SATURDAY = 0.10
SUNDAY = 0.20
FUEL = 2.10
GUIDE = 100

budget = float(input())
qty_fuel = float(input())
day_of_week = input()

fuel_price = qty_fuel * FUEL
total_money = fuel_price + GUIDE

money = 0
total_money_disc = 0

if day_of_week == "Sunday":
    total_money_disc = total_money * SUNDAY
    money = total_money - total_money_disc
elif day_of_week == "Saturday":
    total_money_disc = total_money * SATURDAY
    money = total_money - total_money_disc

left = budget - total_money_disc

if budget > total_money_disc:
    print(f"Safari time! Money left: {left:.2f} lv.")

print(money)
