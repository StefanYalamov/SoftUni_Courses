# Инициализация на променливи
total_tickets = 0  # Общ брой закупени билети
student_tickets = 0  # Брой студентски билети
standard_tickets = 0  # Брой стандартни билети
kids_tickets = 0  # Брой детски билети

# Четене на първоначалния филм
while True:
    movie_name = input()  # Прочитане на името на филма
    if movie_name == "Finish":
        break  # Ако командата е "Finish", приключваме цикъла

    # Прочитане на броя свободни места за текущия филм
    available_seats = int(input())
    sold_tickets_for_movie = 0  # Брой продадени билети за текущия филм

    # Четене на типовете билети за текущия филм
    while sold_tickets_for_movie < available_seats:
        ticket_type = input()
        if ticket_type == "End":
            break  # Ако командата е "End", приключваме продажбите за текущия филм

        # Увеличаваме брояча за съответния тип билет
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1

        # Увеличаваме броя на продадените билети за текущия филм и общо
        sold_tickets_for_movie += 1
        total_tickets += 1

    # Изчисляване на запълнеността на залата за текущия филм
    percentage_full = sold_tickets_for_movie / available_seats * 100
    print(f"{movie_name} - {percentage_full:.2f}% full.")

# Изчисляване на процентите за всеки тип билет
student_percentage = student_tickets / total_tickets * 100
standard_percentage = standard_tickets / total_tickets * 100
kids_percentage = kids_tickets / total_tickets * 100

# Отпечатване на общия резултат
print(f"Total tickets: {total_tickets}")
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kids_percentage:.2f}% kids tickets.")
