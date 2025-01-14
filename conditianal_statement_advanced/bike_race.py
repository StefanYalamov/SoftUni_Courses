JUNIORS_TRAIL_TAX = 5.50
JUNIORS_CROSS_TAX = 8
JUNIORS_DOWN_TAX = 12.25
JUNIORS_ROAD_TAX = 20

SENIORS_TRAIL_TAX = 7
SENIORS_CROSS_TAX = 9.50
SENIORS_DOWN_TAX = 13.75
SENIORS_ROAD_TAX = 21.50

CROSS_50_MORE = 0.25

TOTAL_EXPENSES = 0.05

juniors = int(input())
seniors = int(input())
track_type = input()

total_income = 0

if track_type == "trail":
    total_income = (juniors * JUNIORS_TRAIL_TAX) + (seniors * SENIORS_TRAIL_TAX)
elif track_type == "cross-country":
    total_income = (juniors * JUNIORS_CROSS_TAX) + (seniors * SENIORS_CROSS_TAX)
    if seniors + juniors >= 50:
        total_income = total_income - (total_income * CROSS_50_MORE)

elif track_type == "downhill":
    total_income = (juniors * JUNIORS_DOWN_TAX) + (seniors * SENIORS_DOWN_TAX)

elif track_type == "road":
    total_income = (juniors * JUNIORS_ROAD_TAX) + (seniors * SENIORS_ROAD_TAX)

money_left = total_income - (total_income * TOTAL_EXPENSES)

print(f"{money_left:.2f}")
