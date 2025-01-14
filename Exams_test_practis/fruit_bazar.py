qgoda_price = float(input())
qty_banana = float(input())
qty_oranges = float(input())
qty_malina = float(input())
qty_qgoda = float(input())

malina_price = qgoda_price * 0.50
banana_price = malina_price - (malina_price * 0.80)
orange_price = malina_price - (malina_price * 0.40)

sum_malina = malina_price * qty_malina
sum_oranges = orange_price * qty_oranges
sum_banana = banana_price * qty_banana
sum_qgoda = qgoda_price * qty_qgoda

total_sum = sum_banana + sum_malina + sum_oranges + sum_qgoda

print(f"{total_sum:.2f}")
