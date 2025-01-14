a = int(input())
b = int(input())
max_pass_generated = int(input())

A = 35
B = 64
pass_counter = 0

for x in range(1, a + 1):
    for y in range(1, b + 1):
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
        pass_counter += 1

        A += 1
        B += 1

        if A > 55:
            A= 35

        if B > 96:
            B = 64

        if pass_counter == max_pass_generated:
            break
    if pass_counter == max_pass_generated:
        break
