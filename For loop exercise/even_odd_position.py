# Въвеждане на броя на числата
n = int(input())

# Инициализация на променливи за нечетни позиции
odd_sum = 0.0
odd_min = float('inf')  # Първоначално задаваме най-голяма стойност за минималното число
odd_max = float('-inf')  # Първоначално задаваме най-малка стойност за максималното число

# Инициализация на променливи за четни позиции
even_sum = 0.0
even_min = float('inf')
even_max = float('-inf')

# Обхождане на всяко число според позицията му
for position in range(1, n + 1):
    number = float(input())

    # Проверка дали позицията е нечетна
    if position % 2 == 1:  # Нечетна позиция
        odd_sum += number
        if number < odd_min:
            odd_min = number
        if number > odd_max:
            odd_max = number
    else:  # Четна позиция
        even_sum += number
        if number < even_min:
            even_min = number
        if number > even_max:
            even_max = number

# Проверка дали има стойности на нечетни позиции
if odd_min == float('inf'):
    odd_min = "No"
else:
    odd_min = f"{odd_min:.2f}"

if odd_max == float('-inf'):
    odd_max = "No"
else:
    odd_max = f"{odd_max:.2f}"

# Проверка дали има стойности на четни позиции
if even_min == float('inf'):
    even_min = "No"
else:
    even_min = f"{even_min:.2f}"

if even_max == float('-inf'):
    even_max = "No"
else:
    even_max = f"{even_max:.2f}"

# Принтиране на резултатите с необходимото форматиране
print(f"OddSum={odd_sum:.2f}, OddMin={odd_min}, OddMax={odd_max}, EvenSum={even_sum:.2f}, EvenMin={even_min}, EvenMax={even_max}")
