# Дефиниране на цените за всеки вид цвете в различните сезони
HRISANTEMS_SUMMER = 2.00
HRISANTEMS_WINTER = 3.75

ROSES_SUMMER = 4.10
ROSES_WINTER = 4.50

TULIPS_SUMMER = 2.50
TULIPS_WINTER = 4.15

FLOWERS_ARRANGEMENT = 2.00

# Входни данни
hrisantems = int(input())  # Брой хризантеми
roses = int(input())       # Брой рози
tulips = int(input())      # Брой лалета
season = input()           # Сезон ("Spring", "Summer", "Autumn", "Winter")
weekend = input()          # Уикенд (дали е празничен ден, "Y" или "N")

# Инициализация на цената на цветята
flower_price = 0

# Изчисляване на цената според сезона
if season == "Spring" or season == "Summer":
    flower_price = hrisantems * HRISANTEMS_SUMMER + roses * ROSES_SUMMER + tulips * TULIPS_SUMMER
elif season == "Autumn" or season == "Winter":
    flower_price = hrisantems * HRISANTEMS_WINTER + roses * ROSES_WINTER + tulips * TULIPS_WINTER

# Увеличение на цената, ако е уикенд
if weekend == "Y":
    flower_price = flower_price + (flower_price * 0.15)

# Пролетна отстъпка, ако има 7 или повече лалета
if tulips >= 7 and season == "Spring":
    flower_price -= flower_price * 0.05

# Зимна отстъпка, ако има 10 или повече рози
if roses >= 10 and season == "Winter":
    flower_price -= flower_price * 0.10

# Ако общият брой цветя е над 20, прилагаме допълнителна отстъпка от 20%
total_flowers = hrisantems + roses + tulips
if total_flowers > 20:
    flower_price -= flower_price * 0.20

# Добавяне на таксата за аранжиране
final_price = flower_price + FLOWERS_ARRANGEMENT

# Принтиране на крайната цена с форматиране до втория знак
print(f"{final_price:.2f}")
