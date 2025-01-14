from math import floor
from math import ceil

tennis_rocket_price = float(input())
qty_tennis_rockets = int(input())
qty_sneakers = int(input())


sneakers_price = tennis_rocket_price / 6
sneakers = sneakers_price * qty_sneakers
equipment = (tennis_rocket_price * qty_tennis_rockets + sneakers) * 0.20
total_price = (tennis_rocket_price * qty_tennis_rockets) + sneakers + equipment

jockovich = floor(total_price / 8)
sponsors = ceil(total_price * (7 / 8))


print(f"Price to be paid by Djokovic {jockovich}")
print(f"Price to be paid by sponsors {sponsors}")
