target_amount = int(input())

total_amount = 0
cash_payments = 0
card_payments = 0
cash_count = 0
card_count = 0
cash_turn = True

while total_amount < target_amount:
    command = input()

    if command == "End":
        print("Failed to collect required money for charity.")
        break

    price = int(command)

    if cash_turn:
        if price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cash_payments += price
            cash_count += 1
            total_amount += price

    else:
        if price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            card_payments += price
            card_count += 1
            total_amount += price

    cash_turn = not cash_turn

if total_amount >= target_amount:
    avg_cash = cash_payments / cash_count if cash_count > 0 else 0
    avg_card = card_payments / card_count if card_count > 0 else 0
    print(f"Average CS: {avg_cash:.2f}")
    print(f"Average CC: {avg_card:.2f}")
