# Четене на входните данни
inherited_money = float(input())  # Наследените пари
end_year = int(input())  # Годината, до която трябва да живее

# Иванчо започва от 1800 година и е на 18 години
current_age = 18

# Обхождаме годините от 1800 до крайната година (включително)
for year in range(1800, end_year + 1):
    if year % 2 == 0:  # Четна година
        yearly_expenses = 12000
    else:  # Нечетна година
        yearly_expenses = 12000 + 50 * current_age  # Допълнителен разход според възрастта

    # Приспадаме разходите за текущата година
    inherited_money -= yearly_expenses

    # Увеличаваме възрастта на Иванчо с 1 всяка година
    current_age += 1

# След като обходим всички години, проверяваме дали парите са достатъчни
if inherited_money >= 0:
    # Парите са достатъчни
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    # Парите не достигат
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")
