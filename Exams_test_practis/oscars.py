# Входни данни
actor_name = input()
initial_points = float(input())
number_of_judges = int(input())

# Начални точки на актьора
total_points = initial_points

# Преглеждаме всеки оценяващ
for _ in range(number_of_judges):
    judge_name = input()
    judge_points = float(input())

    # Изчисляваме добавените точки за текущия оценяващ
    additional_points = (len(judge_name) * judge_points) / 2
    total_points += additional_points

    # Проверка дали общите точки надвишават 1250.5
    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    # Ако цикълът завърши без прекъсване, актьорът няма достатъчно точки
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
