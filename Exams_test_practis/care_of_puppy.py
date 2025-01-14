# Въвеждане на началното количество храна в килограми и преобразуване в грамове
total_food_grams = int(input()) * 1000

# Създаваме променлива за натрупване на изядената храна
total_eaten_food = 0

# Четене на всяко хранене, докато не се въведе командата "Adopted"
while True:
    command = input()
    if command == "Adopted":
        break
    food_per_meal = int(command)
    total_eaten_food += food_per_meal

# Проверка дали храната е достатъчна или не
if total_food_grams >= total_eaten_food:
    remaining_food = total_food_grams - total_eaten_food
    print(f"Food is enough! Leftovers: {remaining_food} grams.")
else:
    needed_food = total_eaten_food - total_food_grams
    print(f"Food is not enough. You need {needed_food} grams more.")
