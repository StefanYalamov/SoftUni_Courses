last_sector = input()
qty_rows_first_sector = int(input())
qty_seats_odd_row = int(input())

total_seats = 0

# Цикъл за секторите
for sector in range(ord("A"), ord(last_sector) + 1):
    # Цикъл за редовете във всеки сектор
    for row in range(1, qty_rows_first_sector + (sector - ord("A")) + 1):
        # Определяме броя на местата според четността на реда
        if row % 2 != 0:
            seats_per_row = qty_seats_odd_row  # Нечетен ред
        else:
            seats_per_row = qty_seats_odd_row + 2  # Четен ред

        # Цикъл за местата на всеки ред
        for seat in range(1, seats_per_row + 1):
            print(f"{chr(sector)}{row}{chr(96 + seat)}")  # Отпечатваме мястото
            total_seats += 1  # Увеличаваме броя на местата

# Отпечатваме общия брой на местата
print(total_seats)
