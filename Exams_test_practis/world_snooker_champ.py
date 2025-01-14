# Прочитане на входните данни
stage = input()  # Етап на първенството
ticket_type = input()  # Вид на билета
ticket_count = int(input())  # Брой билети
photo_option = input()  # Опция за снимка ('Y' или 'N')

# Определяне на цената на един билет според етапа и вида
ticket_price = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90
elif stage == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40
elif stage == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400.00

# Изчисляване на общата цена на билетите
total_price = ticket_count * ticket_price

# Прилагане на отстъпки
if total_price > 4000:
    # 25% отстъпка и безплатни снимки
    total_price *= 0.75  # 25% отстъпка
    photo_option = 'N'  # Безплатни снимки
elif total_price > 2500:
    # 10% отстъпка
    total_price *= 0.90  # 10% отстъпка

# Добавяне на таксата за снимка, ако опцията е избрана
if photo_option == 'Y':
    total_price += ticket_count * 40  # 40 лири на билет за снимка

# Отпечатване на крайния резултат, форматиран до втората цифра след десетичната запетая
print(f"{total_price:.2f}")


# Вариант със For цикъл :

# Дефиниране на цените в списъци
stages = ["Quarter final", "Semi final", "Final"]
ticket_types = ["Standard", "Premium", "VIP"]

# Списъци с цени за всеки етап
prices = [
    [55.50, 105.20, 118.90],  # Quarter final: Standard, Premium, VIP
    [75.88, 125.22, 300.40],  # Semi final: Standard, Premium, VIP
    [110.10, 160.66, 400.00]  # Final: Standard, Premium, VIP
]

# Входни данни
stage = input()  # Етап на първенството
ticket_type = input()  # Вид на билета
ticket_count = int(input())  # Брой билети
photo_option = input()  # Опция за снимка ('Y' или 'N')

# Намиране на индекса на етапа с for цикъл
for i in range(len(stages)):
    if stages[i] == stage:
        stage_index = i
        break

# Намиране на индекса на типа билет с for цикъл
for j in range(len(ticket_types)):
    if ticket_types[j] == ticket_type:
        ticket_index = j
        break

# Определяне на цената на един билет
ticket_price = prices[stage_index][ticket_index]

# Изчисляване на общата цена на билетите
total_price = ticket_count * ticket_price

# Прилагане на отстъпки
if total_price > 4000:
    total_price *= 0.75
    photo_option = 'N'
elif total_price > 2500:
    total_price *= 0.90

# Добавяне на таксата за снимка, ако опцията е избрана
if photo_option == 'Y':
    total_price += ticket_count * 40

# Отпечатване на крайния резултат
print(f"{total_price:.2f}")
