product_name = input()
day = input()
quantity = float(input())
price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if product_name == "banana":
        price = 2.50
    elif product_name == "apple":
        price = 1.20
    elif product_name == "orange":
        price = 0.85
    elif product_name == "grapefruit":
        price = 1.45
    elif product_name == "kiwi":
        price = 2.70
    elif product_name == "pineapple":
        price = 5.50
    elif product_name == "grapes":
        price = 3.85

elif day == "Saturday" or day == "Sunday":
    if product_name == "banana":
        price = 2.70
    elif product_name == "apple":
        price = 1.25
    elif product_name == "orange":
        price = 0.90
    elif product_name == "grapefruit":
        price = 1.60
    elif product_name == "kiwi":
        price = 3.00
    elif product_name == "pineapple":
        price = 5.60
    elif product_name == "grapes":
        price = 4.20

else:
    print("error")

total_price = quantity * price

print(f"{total_price:.2f}")

