upper_limit_first = int(input())
upper_limit_second = int(input())
upper_limit_third = int(input())

for first_digit in range(1, upper_limit_first + 1):
    if first_digit % 2 == 0:
        pass

    for second_digit in range(1, upper_limit_second + 1):
        if second_digit == 2 or second_digit == 3 or second_digit == 5 or second_digit == 7:
            pass

        for third_digit in range(1, upper_limit_third + 1):
            if third_digit % 2 == 0:
                print(f"{first_digit} {second_digit} {third_digit}")

# Obqsnena:

upper_limit_first = int(input())
upper_limit_second = int(input())
upper_limit_third = int(input())

# Вложени цикли за всяка цифра
for first_digit in range(1, upper_limit_first + 1):
    if first_digit % 2 == 0:  # Проверка дали първата цифра е четна
        for second_digit in range(2, upper_limit_second + 1):
            if second_digit in [2, 3, 5, 7]:  # Проверка дали втората цифра е просто число
                for third_digit in range(1, upper_limit_third + 1):
                    if third_digit % 2 == 0:  # Проверка дали третата цифра е четна
                        # Отпечатване на валидния PIN код
                        print(f"{first_digit}{second_digit}{third_digit}")
