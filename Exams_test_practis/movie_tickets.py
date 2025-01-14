# Прочитане на входа
a1 = int(input())
a2 = int(input())
n = int(input())

# Обхождане на ASCII символи от a1 до a2 - 1
for symbol1_ascii in range(a1, a2):
    # Проверка дали ASCII кодът на първия символ е нечетен
    if symbol1_ascii % 2 == 1:
        symbol1 = chr(symbol1_ascii)
        symbol4 = symbol1_ascii  # Четвърти символ е ASCII кодът на символ1

        # Обхождане на стойностите за втория символ от 1 до n-1
        for symbol2 in range(1, n):
            # Обхождане на стойностите за третия символ от 1 до n/2 - 1
            for symbol3 in range(1, n // 2):
                # Изчисляване на сумата от символ2 + символ3 + символ4
                total_sum = symbol2 + symbol3 + symbol4

                # Проверка дали сборът е нечетен
                if total_sum % 2 == 1:
                    # Форматиране и отпечатване на билета
                    print(f"{symbol1}-{symbol2}{symbol3}{symbol4}")
