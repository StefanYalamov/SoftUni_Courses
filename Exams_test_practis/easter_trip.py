destination = input()
date_range = input()
number_of_nights = int(input())

price_per_night = 0

if destination == "France":
    if date_range == "21-23":
        price_per_night = 30
    elif date_range == "24-27":
        price_per_night = 35
    elif date_range == "28-31":
        price_per_night = 40

elif destination == "Italy":
    if date_range == "21-23":
        price_per_night = 28
    elif date_range == "24-27":
        price_per_night = 32
    elif date_range == "28-31":
        price_per_night = 39

elif destination == "Germany":
    if date_range == "21-23":
        price_per_night = 32
    elif date_range == "24-27":
        price_per_night = 37
    elif date_range == "28-31":
        price_per_night = 43

total_cost = price_per_night * number_of_nights

print(f"Easter trip to {destination} : {total_cost:.2f} leva.")
