
bottles = int(input())
detergent_available = bottles * 750

washed_dishes = 0
washed_pots = 0
load_count = 0
not_enough_detergent = False

while True:
    command = input()

    if command == "End":
        break

    number_of_dishes = int(command)
    load_count += 1

    if load_count % 3 == 0:
        detergent_needed = number_of_dishes * 15
        washed_pots += number_of_dishes
    else:
        detergent_needed = number_of_dishes * 5
        washed_dishes += number_of_dishes

    if detergent_needed > detergent_available:
        print(f"Not enough detergent, {detergent_needed - detergent_available} ml. more necessary!")
        not_enough_detergent = True
        break

    detergent_available -= detergent_needed

if not not_enough_detergent:
    print("Detergent was enough!")
    print(f"{washed_dishes} dishes and {washed_pots} pots were washed.")
    print(f"Leftover detergent {detergent_available} ml.")
