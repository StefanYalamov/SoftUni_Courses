first_letter = input()
second_letter = input()
third_letter = input()

counter = 0

for first_char in range(ord(first_letter), ord(second_letter) + 1):
    for second_char in range(ord(first_letter), ord(second_letter) + 1):
        for third_char in range(ord(first_letter), ord(second_letter) + 1):
            if chr(first_char) == third_letter or chr(second_char) == third_letter or chr(third_char) == third_letter:
                continue
            print(f"{chr(first_char)}{chr(second_char)}{chr(third_char)}", end=" ")

            counter += 1

print(counter)

# Obqsnena:

first_letter = input()
second_letter = input()
third_letter = input()

counter = 0

# Вложени цикли за обхождане на буквите
for first_char in range(ord(first_letter), ord(second_letter) + 1):
    for second_char in range(ord(first_letter), ord(second_letter) + 1):
        for third_char in range(ord(first_letter), ord(second_letter) + 1):
            # Проверка дали някоя от буквите съвпада с третата буква
            if chr(first_char) == third_letter or chr(second_char) == third_letter or chr(third_char) == third_letter:
                continue  # Пропускаме комбинации, съдържащи третата буква
            # Отпечатване на валидната комбинация
            print(f"{chr(first_char)}{chr(second_char)}{chr(third_char)}", end=" ")
            # Увеличаваме брояча
            counter += 1

# Отпечатваме броя на валидните комбинации
print(counter)
