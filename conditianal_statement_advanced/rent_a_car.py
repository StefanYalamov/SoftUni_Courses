budget = float(input())
season = input()

car_class = ""
car_type = ""
car_price = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_price = budget * 0.35
        car_type = "Cabrio"
    if season == "Winter":
        car_price = budget * 0.65
        car_type = "Jeep"

elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_price = budget * 0.45
        car_type = "Cabrio"
    if season == "Winter":
        car_price = budget * 0.80
        car_type = "Jeep"

if budget > 500:
    car_class = "Luxury class"
    car_price = budget * 0.90
    car_type = "Jeep"

print(f"{car_class}")
print(f"{car_type} - {car_price:.2f}")
