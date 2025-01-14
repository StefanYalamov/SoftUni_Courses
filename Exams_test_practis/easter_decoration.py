# Цени на продуктите в магазина
PRODUCT_PRICES = {
    "basket": 1.50,
    "wreath": 3.80,
    "chocolate bunny": 7.00
}

# Четем броя на клиентите
number_of_clients = int(input())

# Инициализиране на общата сума
total_bill = 0

# Обработваме всеки клиент
for _ in range(number_of_clients):
    items_count = 0  # Брояч за броя артикули за всеки клиент
    current_bill = 0  # Сумата за текущия клиент

    while True:
        product = input()
        if product == "Finish":  # Краят на покупките за текущия клиент
            break
        # Добавяме цената на текущия продукт към сметката на клиента
        current_bill += PRODUCT_PRICES[product]
        items_count += 1

    # Ако броят на закупените артикули е четен, прилагаме отстъпка 20%
    if items_count % 2 == 0:
        current_bill *= 0.80  # Намаляваме сметката с 20%

    # Отпечатваме сметката за текущия клиент
    print(f"You purchased {items_count} items for {current_bill:.2f} leva.")

    # Добавяме сметката на текущия клиент към общата сума
    total_bill += current_bill

# Изчисляваме средната сметка на клиентите
average_bill = total_bill / number_of_clients
# Отпечатваме средната сметка
print(f"Average bill per client is: {average_bill:.2f} leva.")
