n = int(input("Введите число для таблицы умножения: "))
s = list(range(10))
print(f"Таблица умножения для числа {n}:")
for i in s:
    r = n * i
    print(f"{n} x {i} = {r}")
