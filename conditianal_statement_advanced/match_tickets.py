VIP = 499.99
NORMAL = 249.99

budget = float(input())
category = input()
group = int(input())

transport = 0
ticket_price = 0

if 0 < group <= 4:
    transport = budget - (budget * 0.75)
    if category == "Normal":
        ticket_price = NORMAL * group
    elif category == "VIP":
        ticket_price = VIP * group

if 4 < group <= 9:
    transport = budget - (budget * 0.60)
    if category == "Normal":
        ticket_price = NORMAL * group
    elif category == "VIP":
        ticket_price = VIP * group

if 9 < group <= 24:
    transport = budget - (budget * 0.50)
    if category == "Normal":
        ticket_price = NORMAL * group
    elif category == "VIP":
        ticket_price = VIP * group

if 24 < group <= 49:
    transport = budget - (budget * 0.40)
    if category == "Normal":
        ticket_price = NORMAL * group
    elif category == "VIP":
        ticket_price = VIP * group

if group >= 50:
    transport = budget - (budget * 0.25)
    if category == "Normal":
        ticket_price = NORMAL * group
    elif category == "VIP":
        ticket_price = VIP * group

money_left = transport - ticket_price

if transport > ticket_price:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva.")
