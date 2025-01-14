men_clients = int(input())
women_clients = int(input())
qty_tables = int(input())

counter = 0

for man in range(1, men_clients + 1):
    for woman in range(1, women_clients + 1):
        print(f"({man} <-> {woman})", end=" ")
        counter += 1

        if counter == qty_tables:
            break

    if counter == qty_tables:
        break

# Obqsnena:

men_clients = int(input())
women_clients = int(input())
qty_tables = int(input())

counter = 0

for man in range(1, men_clients + 1):
    for woman in range(1, women_clients + 1):
        # Отпечатваме срещата със скоби
        print(f"({man} <-> {woman})", end=" ")
        counter += 1

        # Проверяваме дали сме достигнали лимита на масите
        if counter == qty_tables:
            break  # Прекъсваме вътрешния цикъл, ако достигнем лимита
    if counter == qty_tables:
        break  # Прекъсваме и външния цикъл, ако достигнем лимита
