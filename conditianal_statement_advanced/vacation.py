budget = float(input())
season = input()

vacation_type = ""
location = ""
price = 0

if budget <= 1000:
    vacation_type = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    if season == "Winter":
        location = "Morocco"
        price = budget * 0.45

if 1000 < budget <= 3000:
    vacation_type = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    if season == "Winter":
        location = "Morocco"
        price = budget * 0.60

if budget > 3000:
    vacation_type = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    if season == "Winter":
        location = "Morocco"
        price = budget * 0.90

print(f"{location} - {vacation_type} - {price:.2f}")
