# Прочитане на входа
rent = int(input())  # Наем за залата

# Изчисляване на разходите
statuettes = rent * 0.70  # Статуетките са 30% по-малко от наема
catering = statuettes * 0.85  # Кетърингът е 15% по-малко от статуетките
sound = catering * 0.50  # Озвучаването е 50% от цената на кетъринга

# Обща сума за разходите
total_cost = rent + statuettes + catering + sound

# Отпечатване на резултата
print(f"{total_cost:.2f}")
