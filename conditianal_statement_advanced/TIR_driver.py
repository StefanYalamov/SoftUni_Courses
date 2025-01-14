TAXES = 0.10

SPRING_AUTUMN_TO_5000 = 0.75
SPRING_AUTUMN_TO_10000 = 0.95

SUMMER_TO_5000 = 0.90
SUMMER_TO_10000 = 1.10

WINTER_TO_5000 = 1.05
WINTER_TO_10000 = 1.25

_TO_20000 = 1.45

SEASON_DURATION = 4

season = input()
km_per_month = float(input())

salary = 0

if km_per_month <= 5000:
    if season == "Spring" or "Autumn":
        salary = SPRING_AUTUMN_TO_5000 * km_per_month
    if season == "Summer":
        salary = SUMMER_TO_5000 * km_per_month
    if season == "Winter":
        salary = WINTER_TO_5000 * km_per_month

elif km_per_month <= 10000:
    if season == "Spring" or "Autumn":
        salary = SPRING_AUTUMN_TO_10000 * km_per_month
    if season == "Summer":
        salary = SUMMER_TO_10000 * km_per_month
    if season == "Winter":
        salary = WINTER_TO_10000 * km_per_month

elif km_per_month <= 20000:
    if season == "Spring" or "Autumn" or "Summer" or "Winter":
        salary = _TO_20000 * km_per_month

salary_season = salary * SEASON_DURATION

salary_tax = salary_season - (salary_season * 0.10)

print(f"{salary_tax:.2f}")
