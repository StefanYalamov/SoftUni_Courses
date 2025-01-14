# Входни данни
contract_term = input()  # Срок на договора: "one" или "two"
contract_type = input()  # Тип на договора: "Small", "Middle", "Large", или "ExtraLarge"
internet = input()       # Добавен мобилен интернет: "yes" или "no"
months = int(input())    # Брой месеци: цяло число в интервала [1 … 24]

# Определяне на месечната такса според срока и типа на договора
monthly_fee = 0

if contract_term == "one":
    if contract_type == "Small":
        monthly_fee = 9.98
    elif contract_type == "Middle":
        monthly_fee = 18.99
    elif contract_type == "Large":
        monthly_fee = 25.98
    elif contract_type == "ExtraLarge":
        monthly_fee = 35.99
elif contract_term == "two":
    if contract_type == "Small":
        monthly_fee = 8.58
    elif contract_type == "Middle":
        monthly_fee = 17.09
    elif contract_type == "Large":
        monthly_fee = 23.59
    elif contract_type == "ExtraLarge":
        monthly_fee = 31.79

# Добавяне на цена за мобилен интернет, ако има такъв
if internet == "yes":
    if monthly_fee <= 10:
        monthly_fee += 5.50
    elif monthly_fee <= 30:
        monthly_fee += 4.35
    else:
        monthly_fee += 3.85

# Изчисляване на общата сума
total_price = monthly_fee * months

# Ако договорът е за 2 години, прилагаме отстъпка 3.75%
if contract_term == "two":
    total_price -= total_price * 0.0375

# Отпечатваме крайната цена, форматирана до втория знак
print(f"{total_price:.2f} lv.")
