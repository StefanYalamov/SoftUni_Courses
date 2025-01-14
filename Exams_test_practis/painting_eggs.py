# Константи за цените на различните комбинации
PRICES = {
    "Large": {"Red": 16, "Green": 12, "Yellow": 9},
    "Medium": {"Red": 13, "Green": 9, "Yellow": 7},
    "Small": {"Red": 9, "Green": 8, "Yellow": 5}
}

# Четене на входа
size = input()
color = input()
batch_count = int(input())

# Намиране на цената за избраната комбинация
price_per_batch = PRICES[size][color]

# Изчисляване на общите приходи и разходи
total_price = batch_count * price_per_batch
expenses = total_price * 0.35
final_price = total_price - expenses

# Форматиране и извеждане на резултата
print(f"{final_price:.2f} leva.")
