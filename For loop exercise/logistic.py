# Четене на входните данни
num_cargos = int(input())  # Броят на товарите
total_tons = 0  # Общо тегло на всички товари
total_cost = 0  # Обща цена за транспортиране на всички товари

# Променливи за обем на товари с микробус, камион и влак
minibus_tons = 0
truck_tons = 0
train_tons = 0

# Обхождаме всеки товар
for _ in range(num_cargos):
    tonnage = int(input())  # Тегло на текущия товар
    total_tons += tonnage  # Добавяме към общото тегло

    # Проверяваме с какво превозно средство ще се транспортира товарът
    if tonnage <= 3:
        minibus_tons += tonnage
        total_cost += tonnage * 200  # Цена за микробус (200 лв/тон)
    elif 4 <= tonnage <= 11:
        truck_tons += tonnage
        total_cost += tonnage * 175  # Цена за камион (175 лв/тон)
    else:
        train_tons += tonnage
        total_cost += tonnage * 120  # Цена за влак (120 лв/тон)

# Изчисляваме средната цена на тон за всички товари
average_price_per_ton = total_cost / total_tons

# Изчисляваме процента на тоновете за всяко превозно средство
minibus_percent = (minibus_tons / total_tons) * 100
truck_percent = (truck_tons / total_tons) * 100
train_percent = (train_tons / total_tons) * 100

# Принтираме резултатите, форматирани до втория знак след десетичната запетая
print(f"{average_price_per_ton:.2f}")  # Средната цена на тон
print(f"{minibus_percent:.2f}%")  # Процентът от тоновете с микробус
print(f"{truck_percent:.2f}%")  # Процентът от тоновете с камион
print(f"{train_percent:.2f}%")  # Процентът от тоновете с влак
