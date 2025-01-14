# Прочитане на входните данни
voucher_value = int(input())  # Стойността на ваучера
film_tickets = 0  # Брой на закупените билети
other_purchases = 0  # Брой на закупените други продукти

# Започваме да четем покупките
while True:
    purchase = input()  # Прочитане на името на покупката

    # Проверка за край на цикъла
    if purchase == "End":
        break

    # Определяне на цената на покупката
    if len(purchase) > 8:
        # Филм - цената е сумата на ASCII стойностите на първите два символа
        purchase_price = ord(purchase[0]) + ord(purchase[1])
        # Проверка дали може да си позволи тази покупка
        if voucher_value >= purchase_price:
            voucher_value -= purchase_price  # Намаляване на наличната сума
            film_tickets += 1  # Увеличаване на броя на закупените билети
        else:
            break
    else:
        # Продукт - цената е ASCII стойността на първия символ
        purchase_price = ord(purchase[0])
        # Проверка дали може да си позволи тази покупка
        if voucher_value >= purchase_price:
            voucher_value -= purchase_price  # Намаляване на наличната сума
            other_purchases += 1  # Увеличаване на броя на закупените продукти
        else:
            break

# Отпечатване на резултатите
print(f"{film_tickets}")
print(f"{other_purchases}")
