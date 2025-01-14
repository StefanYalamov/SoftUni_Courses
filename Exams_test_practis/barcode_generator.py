# Четем входните данни
start = input()
end = input()

# За всяка цифра от четирицифреното число, взимаме диапазона от съответните позиции
for i1 in range(int(start[0]), int(end[0]) + 1):
    for i2 in range(int(start[1]), int(end[1]) + 1):
        for i3 in range(int(start[2]), int(end[2]) + 1):
            for i4 in range(int(start[3]), int(end[3]) + 1):
                # Проверяваме дали всички цифри са нечетни
                if i1 % 2 != 0 and i2 % 2 != 0 and i3 % 2 != 0 and i4 % 2 != 0:
                    # Отпечатваме резултата, форматиран като баркод
                    print(f"{i1}{i2}{i3}{i4}", end=" ")
