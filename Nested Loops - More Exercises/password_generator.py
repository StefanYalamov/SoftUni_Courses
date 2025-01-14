# Четене на входа
n = int(input())  # Определя диапазона на числата (1 до n)
l = int(input())  # Определя колко от първите букви от латинската азбука ще използваме

# Обхождаме всички възможни комбинации
for first_digit in range(1, n + 1):
    for second_digit in range(1, n + 1):
        for third_char in range(ord('a'), ord('a') + l):  # Обхождаме първите l букви
            for fourth_char in range(ord('a'), ord('a') + l):  # Обхождаме първите l букви
                for fifth_digit in range(1, n + 1):
                    # Проверяваме дали петият символ е по-голям от първия и втория
                    if fifth_digit > first_digit and fifth_digit > second_digit:
                        # Отпечатваме комбинацията
                        print(f"{first_digit}{second_digit}{chr(third_char)}{chr(fourth_char)}{fifth_digit}", end=" ")
