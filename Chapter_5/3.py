gold_prices_2 = [200, 180, 220, 160, 240, 260, 210]

min_price = float('inf')
max_profit = 0

for price in gold_prices_2:
    if price < min_price:
        min_price = price
    current_profit = price - min_price
    if current_profit > max_profit:
        max_profit = current_profit

print("Максимальная прибыль для gold_prices_2:", max_profit)  
