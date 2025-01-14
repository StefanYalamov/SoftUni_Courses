# Въвеждаме началото и края на интервала, както и магическото число
start = int(input())  # Начало на интервала
end = int(input())    # Край на интервала
magic_number = int(input())  # Магическото число

# Инициализираме брояч за комбинациите и флаг, който показва дали сме намерили съвпадение
combination_number = 0
found = False

# Двойно вложен цикъл за генериране на всички двойки в дадения интервал
for x1 in range(start, end + 1):
    for x2 in range(start, end + 1):
        combination_number += 1  # Увеличаваме броя на комбинациите
        if x1 + x2 == magic_number:  # Проверяваме дали сумата на двойката е равна на магическото число
            print(f"Combination N:{combination_number} ({x1} + {x2} = {magic_number})")
            found = True  # Означаваме, че сме намерили комбинацията
            break  # Прекъсваме вътрешния цикъл
    if found:
        break  # Прекъсваме и външния цикъл

# Ако не е намерена нито една комбинация, която да отговаря на условията
if not found:
    print(f"{combination_number} combinations - neither equals {magic_number}")
