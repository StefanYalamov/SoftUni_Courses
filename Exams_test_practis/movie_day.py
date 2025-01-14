# Входни данни
total_time = int(input())  # Време за снимки в минути
scenes = int(input())      # Брой сцени
scene_time = int(input())  # Времетраене на сцена

# Изчисляване на времето за подготовка на терена (15% от общото време)
prep_time = total_time * 0.15

# Изчисляване на общото време за заснемане на сцените
shooting_time = scenes * scene_time

# Общо необходимо време
total_needed_time = prep_time + shooting_time

# Проверка дали времето е достатъчно и отпечатване на резултата
if total_needed_time <= total_time:
    remaining_time = round(total_time - total_needed_time)
    print(f"You managed to finish the movie on time! You have {remaining_time} minutes left!")
else:
    needed_time = round(total_needed_time - total_time)
    print(f"Time is up! To complete the movie you need {needed_time} minutes.")
