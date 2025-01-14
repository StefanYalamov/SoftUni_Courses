upper_limit_hungrets = int(input())
upper_limit_tens = int(input())
upper_limit_ones = int(input())

for hundres in range(1, upper_limit_hungrets + 1):
    if hundres % 2 == 0:
        for tens in range(1, upper_limit_tens + 1):
            if tens in [2, 3, 5, 7]:
                for ones in range(1, upper_limit_ones + 1):
                    if ones % 2 == 0:
                        print(f"{hundres} {tens} {ones}")
