# Прочитане на имената на играчите
player1 = input()
player2 = input()

# Инициализиране на броячите за точки
player1_points = 0
player2_points = 0

# Стартиране на играта с while цикъл
while True:
    # Прочитане на картите на играчите или команда "End of game"
    command = input()

    if command == "End of game":
        # Играта приключва
        print(f"{player1} has {player1_points} points")
        print(f"{player2} has {player2_points} points")
        break

    # Първият играч дава карта
    player1_card = int(command)
    # Вторият играч дава карта
    player2_card = int(input())

    # Проверка на картите
    if player1_card > player2_card:
        # Първият играч печели раздаването
        player1_points += player1_card - player2_card
    elif player2_card > player1_card:
        # Вторият играч печели раздаването
        player2_points += player2_card - player1_card
    else:
        # Равенство -> Number wars!
        print("Number wars!")
        # Прочитане на нови карти за решаване на Number wars!
        player1_card = int(input())  # Нова карта за първия играч
        player2_card = int(input())  # Нова карта за втория играч

        # Играчът с по-висока нова карта печели играта
        if player1_card > player2_card:
            print(f"{player1} is winner with {player1_points} points")
        else:
            print(f"{player2} is winner with {player2_points} points")
        # Прекратяване на играта
        break
