# Входни данни
eggs_player_one = int(input())
eggs_player_two = int(input())

# Стартиране на играта
while True:
    command = input()

    # Проверка за край на играта
    if command == "End":
        print(f"Player one has {eggs_player_one} eggs left.")
        print(f"Player two has {eggs_player_two} eggs left.")
        break

    # Обработка на командите
    if command == "one":
        eggs_player_two -= 1
    elif command == "two":
        eggs_player_one -= 1

    # Проверка за изчерпване на яйцата
    if eggs_player_one == 0:
        print(f"Player one is out of eggs. Player two has {eggs_player_two} eggs left.")
        break
    elif eggs_player_two == 0:
        print(f"Player two is out of eggs. Player one has {eggs_player_one} eggs left.")
        break
