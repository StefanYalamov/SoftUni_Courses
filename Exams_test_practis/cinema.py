# Прочитане на капацитета на залата
capacity = int(input())  # Капацитет на залата
total_income = 0  # Общи приходи от билети
total_people = 0  # Общо влезли хора

while True:
    # Четене на командата или броя на хората
    command = input()

    # Ако командата е "Movie time!", прекратяваме цикъла
    if command == "Movie time!":
        print(f"There are {capacity - total_people} seats left in the cinema.")
        break

    # Брой хора, които влизат в залата
    people_entering = int(command)

    # Проверка дали има достатъчно места за хората
    if total_people + people_entering > capacity:
        print("The cinema is full.")
        break

    # Увеличаваме броя на хората в залата
    total_people += people_entering

    # Изчисляване на приходите за тази група
    current_income = people_entering * 5

    # Ако броят на хората в групата е кратен на 3, добавяме отстъпка от 5 лева
    if people_entering % 3 == 0:
        current_income -= 5

    # Добавяне на приходите към общата сума
    total_income += current_income

# Отпечатване на общия приход
print(f"Cinema income - {total_income} lv.")
