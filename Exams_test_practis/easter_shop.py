# Входни данни
initial_eggs = int(input())  # Началният брой на яйцата
sold_eggs = 0  # Брояч за продадените яйца

# Четем командите, докато не получим "Close"
while True:
    command = input()  # Четем командата
    if command == "Close":
        # Ако командата е "Close", приключваме и показваме резултатите
        print("Store is closed!")
        print(f"{sold_eggs} eggs sold.")
        break

    quantity = int(input())  # Четем количеството за покупка или допълване

    if command == "Buy":
        if initial_eggs >= quantity:
            # Ако има достатъчно яйца, извършваме покупката
            initial_eggs -= quantity
            sold_eggs += quantity
        else:
            # Ако няма достатъчно яйца, прекратяваме с грешка
            print("Not enough eggs in store!")
            print(f"You can buy only {initial_eggs}.")
            break
    elif command == "Fill":
        # Увеличаваме наличността
        initial_eggs += quantity
