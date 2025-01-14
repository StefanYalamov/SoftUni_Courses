one_lev_coin = int(input())
two_leva_coin = int(input())
five_leva_money = int(input())
total_money = int(input())

for one in range(0, one_lev_coin + 1):
    for two in range(0, two_leva_coin + 1):
        for five in range(0, five_leva_money + 1):
            if one * 1 + two * 2 + five * 5 == total_money:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {total_money} lv.")
