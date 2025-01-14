# Функция за проверка дали дадено число е просто
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Прочитане на входа
start_first_pair = int(input())
start_second_pair = int(input())
diff_first_pair = int(input())
diff_second_pair = int(input())

# Крайни стойности на двойките
end_first_pair = start_first_pair + diff_first_pair
end_second_pair = start_second_pair + diff_second_pair

# Обхождаме първата и втората двойка числа в съответния диапазон
for first_pair in range(start_first_pair, end_first_pair + 1):
    for second_pair in range(start_second_pair, end_second_pair + 1):
        # Проверяваме дали и двете двойки числа са прости
        if is_prime(first_pair) and is_prime(second_pair):
            # Отпечатваме валидната комбинация
            print(f"{first_pair}{second_pair}")
