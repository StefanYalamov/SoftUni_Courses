# Входни данни
series_name = input()
num_seasons = int(input())
num_episodes_per_season = int(input())
episode_length = float(input())

# Изчисляване на времето за един епизод с реклами
ad_time = episode_length * 0.20
total_episode_time = episode_length + ad_time

# Общо време за всички обикновени епизоди
total_time = num_seasons * num_episodes_per_season * total_episode_time

# Добавяне на времето за специалните епизоди
total_time += num_seasons * 10

# Закръгляване и отпечатване на резултата
print(f"Total time needed to watch the {series_name} series is {int(total_time)} minutes.")
