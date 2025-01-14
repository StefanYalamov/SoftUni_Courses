# Вход: бюджетът за покупки
budget = float(input())

# Инициализация на променливи
total_spent = 0  # Общата сума за покупките
product_count = 0  # Брояч за броя на закупените продукти

# Четем входни данни за продуктите, докато не получим "Stop"
while True:
    # Четене на името на продукта
    product_name = input()

    # Проверка за командата "Stop"
    if product_name == "Stop":
        print(f"You bought {product_count} products for {total_spent:.2f} leva.")
        break

    # Четене на цената на продукта
    product_price = float(input())
    product_count += 1  # Увеличаваме броя на продуктите

    # Прилагане на отстъпката, ако продуктът е трети поред
    if product_count % 3 == 0:
        product_price /= 2  # Всеки трети продукт е на половин цена

    # Проверка дали текущият продукт може да бъде закупен с наличния бюджет
    if budget < product_price:
        print("You don't have enough money!")
        print(f"You need {product_price - budget:.2f} leva!")
        break

    # Ако бюджетът е достатъчен, намаляваме наличния бюджет
    budget -= product_price
    total_spent += product_price  # Добавяме цената на продукта към общата сума
