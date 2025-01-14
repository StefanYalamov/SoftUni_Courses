week_day = input()
ticket_price = 0

if week_day == "Monday" or week_day == "Tuesday" or week_day == "Friday":
    ticket_price = 12

elif week_day == "Wednesday" or week_day == "Thursday":
    ticket_price = 14

elif week_day == "Saturday" or week_day == "Sunday":
    ticket_price = 16

print(ticket_price)
