# Дефиниране на цените според сезона и типа група
INDIVIDUALS_GROUP_WINTER = 9.60
INDIVIDUALS_GROUP_SPRING = 7.20
INDIVIDUALS_GROUP_SUMMER = 15

MIX_GROUP_WINTER = 10
MIX_GROUP_SPRING = 9.50
MIX_GROUP_SUMMER = 20

DISC_50_MORE = 0.50
DISC_20_50 = 0.15
DISC_10_20 = 0.05

# Въвеждане на данни
season = input()
group_type = input()
qty_students = int(input())
qty_nights = int(input())

# Инициализация на променливи
price = 0
sport_type = ""
total_price = 0

# Изчисляване на цената и избор на спорт според сезона и типа на групата
if season == "Winter":
    if group_type == "boys":
        sport_type = "Judo"
        price = INDIVIDUALS_GROUP_WINTER * qty_students * qty_nights
    elif group_type == "girls":
        sport_type = "Gymnastics"  # Поправка на грешката "Gimnastics" на "Gymnastics"
        price = INDIVIDUALS_GROUP_WINTER * qty_students * qty_nights
    elif group_type == "mixed":
        sport_type = "Ski"
        price = MIX_GROUP_WINTER * qty_students * qty_nights

elif season == "Spring":
    if group_type == "boys":
        sport_type = "Tennis"
        price = INDIVIDUALS_GROUP_SPRING * qty_students * qty_nights
    elif group_type == "girls":
        sport_type = "Athletics"
        price = INDIVIDUALS_GROUP_SPRING * qty_students * qty_nights
    elif group_type == "mixed":
        sport_type = "Cycling"
        price = MIX_GROUP_SPRING * qty_students * qty_nights

elif season == "Summer":
    if group_type == "boys":
        sport_type = "Football"
        price = INDIVIDUALS_GROUP_SUMMER * qty_students * qty_nights
    elif group_type == "girls":
        sport_type = "Volleyball"
        price = INDIVIDUALS_GROUP_SUMMER * qty_students * qty_nights
    elif group_type == "mixed":
        sport_type = "Swimming"
        price = MIX_GROUP_SUMMER * qty_students * qty_nights

# Приложение на отстъпки според броя на учениците
if qty_students >= 50:
    total_price = price - (price * DISC_50_MORE)
elif 20 <= qty_students < 50:  # Използваме elif, за да се прилага само едно отстъпка
    total_price = price - (price * DISC_20_50)
elif 10 <= qty_students < 20:  # Използваме elif, за да се прилага само едно отстъпка
    total_price = price - (price * DISC_10_20)
else:
    total_price = price

# Принтиране на крайния резултат
print(f"{sport_type} {total_price:.2f} lv.")
