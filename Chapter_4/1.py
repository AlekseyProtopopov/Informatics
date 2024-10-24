import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропускаем заголовок, если он есть
        total_cost = sum(float(row[1]) for row in reader if row)  # Суммируем стоимости
    return total_cost

# Пример вызова функции
cost = portfolio_cost('data/portfolio.csv')
print('Total cost:', cost)
