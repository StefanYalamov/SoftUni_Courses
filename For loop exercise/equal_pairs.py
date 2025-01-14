# Въвеждане на броя на двойките
n = int(input())

# Инициализация на променливи
previous_sum = None  # Стойността на предишната двойка
max_diff = 0  # Максимална разлика между последователни двойки
all_equal = True  # Флаг, който проверява дали всички стойности са равни
first_pair_value = 0  # Стойност на първата двойка

# Обхождане на всички двойки
for i in range(n):
    # Въвеждане на стойностите на двете числа в двойката
    first_number = int(input())
    second_number = int(input())

    # Изчисляване на сумата на текущата двойка
    current_sum = first_number + second_number

    # Записваме стойността на първата двойка
    if i == 0:
        first_pair_value = current_sum
    else:
        # Изчисляваме разликата спрямо предишната двойка и проверяваме дали е най-голямата досега
        difference = abs(current_sum - previous_sum)
        if difference > max_diff:
            max_diff = difference

        # Ако текущата стойност не е равна на първата, задаваме флага на False
        if current_sum != first_pair_value:
            all_equal = False

    # Запазваме текущата стойност като "предишна" за следващата итерация
    previous_sum = current_sum

# Извеждане на резултата
if all_equal:
    print(f"Yes, value={first_pair_value}")
else:
    print(f"No, maxdiff={max_diff}")
