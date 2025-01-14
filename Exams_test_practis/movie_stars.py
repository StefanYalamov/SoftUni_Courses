# Четене на първоначалния бюджет
budget = float(input())

# Променлива за проследяване на оставащия бюджет
remaining_budget = budget

# Започваме да четем входни данни за актьорите
while True:
    actor_name = input()  # Четене на името на актьора

    # Ако получим командата "ACTION", прекъсваме четенето
    if actor_name == "ACTION":
        print(f"We are left with {remaining_budget:.2f} leva.")
        break

    # Проверяваме дали името е по-дълго от 15 символа
    if len(actor_name) > 15:
        # Ако е по-дълго, заплатата е 20% от текущия бюджет
        salary = remaining_budget * 0.20
    else:
        # Ако не е, четем следващия ред за заплатата
        salary = float(input())

    # Намаляване на оставащия бюджет
    remaining_budget -= salary

    # Проверка дали бюджетът е изчерпан
    if remaining_budget < 0:
        print(f"We need {abs(remaining_budget):.2f} leva for our actors.")
        break
