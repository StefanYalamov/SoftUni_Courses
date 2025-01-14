# Въвеждане на входните данни
bitcoins = int(input())                # Броят биткойни
yuan = float(input())                  # Броят китайски юани
commission = float(input())            # Комисионната в проценти

# Изчисляване на стойностите в лева
bitcoin_to_leva = bitcoins * 1168                  # Конвертиране на биткойните в лева
yuan_to_dollars = yuan * 0.15                      # Конвертиране на юаните в долари
yuan_to_leva = yuan_to_dollars * 1.76              # Конвертиране на доларите в лева

# Обща стойност в лева
total_leva = bitcoin_to_leva + yuan_to_leva

# Конвертиране на левовете в евро
total_euro = total_leva / 1.95

# Прилагане на комисионната
final_amount = total_euro - (total_euro * commission / 100)

# Извеждане на резултата
print(f"{final_amount:.2f}")
