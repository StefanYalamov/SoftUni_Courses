start_count = int(input())
end_count = int(input())
magic_number = int(input())

combination_count = 0
found = False

for start in range(start_count, end_count + 1):
    for end in range(start_count, end_count + 1):
        combination_count += 1
        if start + end == magic_number:
            print(f"Combination N:{combination_count} ({start} + {end} = {magic_number})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{combination_count} combinations - neither equals {magic_number}")
