# Променливи за цени и отстъпки
WINDOW_PRICES = {
    "90X130": 110,
    "100X150": 140,
    "130X180": 190,
    "200X300": 250
}

DISCOUNTS = {
    "90X130": {30: 0.05, 60: 0.08},
    "100X150": {40: 0.06, 80: 0.10},
    "130X180": {20: 0.07, 50: 0.12},
    "200X300": {25: 0.09, 50: 0.14}
}

DELIVERY_COST = 60
LARGE_ORDER_DISCOUNT = 0.04

# Четене на входни данни
qty_windows = int(input())  # Брой дограми
window_type = input()       # Вид на дограмите
delivery_type = input()     # Начин на получаване ("With delivery" или "Without delivery")

# Проверка дали поръчката е валидна
if qty_windows < 10:
    print("Invalid order")
else:
    # Изчисляване на базовата цена
    base_price = WINDOW_PRICES[window_type]
    total_price = base_price * qty_windows

    # Проверка и прилагане на отстъпки спрямо количеството
    if qty_windows in DISCOUNTS[window_type]:
        discount = DISCOUNTS[window_type][qty_windows]
    else:
        # Търсим най-голямата отстъпка за текущото количество
        discount = 0
        for threshold, discount_rate in DISCOUNTS[window_type].items():
            if qty_windows >= threshold:
                discount = discount_rate

    # Прилагане на отстъпката върху общата сума
    total_price -= total_price * discount

    # Добавяне на такса за доставка, ако е избрана
    if delivery_type == "With delivery":
        total_price += DELIVERY_COST

    # Допълнителна отстъпка за големи поръчки (над 99 броя)
    if qty_windows > 99:
        total_price -= total_price * LARGE_ORDER_DISCOUNT

    # Отпечатване на крайния резултат, форматиран до втория знак
    print(f"{total_price:.2f} BGN")
