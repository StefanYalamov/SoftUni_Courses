start_digit = int(input())
end_digit = int(input())

for first_digit in range(start_digit, end_digit + 1):
    for second_digit in range(start_digit, end_digit + 1):
        for third_digit in range(start_digit, end_digit + 1):
            for forth_digit in range(start_digit, end_digit + 1):
                if (first_digit % 2 == 0 and forth_digit % 2 != 0) or (first_digit % 2 != 0 and forth_digit % 2 == 0):
                    if first_digit > forth_digit:
                        if (second_digit + third_digit) % 2 == 0:
                            print(f"{first_digit}{second_digit}{third_digit}{forth_digit}", end=" ")

# Obqsnena:

start_digit = int(input())
end_digit = int(input())

# Брояч за масите
for first_digit in range(start_digit, end_digit + 1):
    for second_digit in range(start_digit, end_digit + 1):
        for third_digit in range(start_digit, end_digit + 1):
            for forth_digit in range(start_digit, end_digit + 1):
                # Проверка дали първата е четна и последната нечетна или обратното
                if (first_digit % 2 == 0 and forth_digit % 2 != 0) or (first_digit % 2 != 0 and forth_digit % 2 == 0):
                    # Проверка дали първата цифра е по-голяма от последната
                    if first_digit > forth_digit:
                        # Проверка дали сумата на втората и третата цифра е четна
                        if (second_digit + third_digit) % 2 == 0:
                            # Отпечатване на валидното число
                            print(f"{first_digit}{second_digit}{third_digit}{forth_digit}", end=" ")
