n = int(input())

for first_digit in range(1, 9 + 1):
    pass
    for second_digit in range(1, 9 + 1):
        pass
        for third_digit in range(1, 9 + 1):
            pass
            for forth_digit in range(1, 9 + 1):
                if first_digit + second_digit == third_digit + forth_digit:
                    if n % (first_digit + second_digit) == 0:
                        print(f"{first_digit}{second_digit}{third_digit}{forth_digit}", end=" ")

# Obqsnena:

n = int(input())

for first_digit in range(1, 9 + 1):
    for second_digit in range(1, 9 + 1):
        for third_digit in range(1, 9 + 1):
            for forth_digit in range(1, 9 + 1):
                # Проверка дали сборът на първите две цифри е равен на сбора на последните две
                if first_digit + second_digit == third_digit + forth_digit:
                    # Проверка дали N се дели без остатък на сбора на първите две цифри
                    if n % (first_digit + second_digit) == 0:
                        # Отпечатване на валидното число
                        print(f"{first_digit}{second_digit}{third_digit}{forth_digit}", end=" ")
