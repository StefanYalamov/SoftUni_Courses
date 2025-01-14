# Прочитане на желаната височина
desired_height = int(input())

# Начална височина е 30 см по-ниска от желаната
current_height = desired_height - 30

# Инициализиране на броячите
total_jumps = 0
failed_attempts = 0

# Цикъл за скоковете на Тихомир
while current_height <= desired_height:
    jump_height = int(input())  # Прочитане на височината на скока
    total_jumps += 1  # Увеличаване на броя на скоковете

    if jump_height > current_height:
        # Успешен скок - повдигаме летвата
        if current_height == desired_height:
            print(f"Tihomir succeeded, he jumped over {current_height}cm after {total_jumps} jumps.")
            break
        # Ако не е достигната желаната височина, повдигаме летвата с 5 см
        current_height += 5
        failed_attempts = 0  # Нулиране на неуспешните опити
    else:
        # Неуспешен скок
        failed_attempts += 1

        # Проверка за три последователни неуспешни скока на същата височина
        if failed_attempts == 3:
            print(f"Tihomir failed at {current_height}cm after {total_jumps} jumps.")
            break
