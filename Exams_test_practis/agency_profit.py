CHILD_TICKET_PRICE = 0.70
AGENCY_PROFIT_TOTAL = 0.20

aeroline = input()
qty_adults_tickets = int(input())
qty_child_tickets = int(input())
adult_ticket_price = float(input())
extra_tax = float(input())

net_child_ticket = adult_ticket_price - CHILD_TICKET_PRICE
adult_ticket_plus_tax = adult_ticket_price + extra_tax
child_ticket_plus_tax = net_child_ticket + extra_tax
total_tickets_price = (qty_adults_tickets * adult_ticket_plus_tax) + (qty_child_tickets * child_ticket_plus_tax)
total_profit = total_tickets_price * AGENCY_PROFIT_TOTAL

print(f"The profit of your agency from {aeroline} tickets is {total_profit:.2f} lv.")

# Решение с помошник:

# Константи
AGENCY_PROFIT_TOTAL = 0.20  # Печалба на агенцията (20%)

# Входни данни
aeroline = input()  # Име на авиокомпанията
qty_adults_tickets = int(input())  # Брой билети за възрастни
qty_child_tickets = int(input())  # Брой детски билети
adult_ticket_price = float(input())  # Нетна цена на билет за възрастен
extra_tax = float(input())  # Цена на такса обслужване

# Правилно изчисление на детски билет: 30% от цената на билета за възрастен
net_child_ticket = adult_ticket_price * 0.30

# Добавяне на таксата към крайната цена на билетите
adult_ticket_plus_tax = adult_ticket_price + extra_tax
child_ticket_plus_tax = net_child_ticket + extra_tax

# Общо за всички билети
total_tickets_price = (qty_adults_tickets * adult_ticket_plus_tax) + (qty_child_tickets * child_ticket_plus_tax)

# Печалба на агенцията
total_profit = total_tickets_price * AGENCY_PROFIT_TOTAL

# Форматиране и печат
print(f"The profit of your agency from {aeroline} tickets is {total_profit:.2f} lv.")
