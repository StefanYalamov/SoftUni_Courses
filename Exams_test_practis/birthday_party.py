
rent = float(input())

cake_price = rent * 0.20
drinks_price = cake_price * 0.55
animator_price = rent / 3

total_budget = rent + cake_price + drinks_price + animator_price

print(f"{total_budget:.2f}")
