# Вход: периодът на дните
period = int(input())  # Броят на дните за наблюдение

# Начален брой лекари
doctors = 7

# Променливи за броене на прегледани и непрегледани пациенти
treated_patients = 0
untreated_patients = 0

# Обхождаме всеки ден
for day in range(1, period + 1):
    # Въвеждане на броя на пациентите за текущия ден
    daily_patients = int(input())

    # Всеки трети ден проверяваме дали да назначим нов лекар
    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1  # Назначаваме още един лекар

    # Изчисляваме прегледаните и непрегледаните пациенти за текущия ден
    if daily_patients <= doctors:
        treated_patients += daily_patients  # Всички пациенти са прегледани
    else:
        treated_patients += doctors  # Преглеждаме само толкова, колкото са наличните лекари
        untreated_patients += daily_patients - doctors  # Останалите са непрегледани

# Принтираме резултатите
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
