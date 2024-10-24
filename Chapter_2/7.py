radius = float(input("Введите радиус окружности: "))
diameter = radius * 2
print(f"Диаметр окружности: {diameter}")
sum_100_to_500 = sum(range(100, 501))
print(f"Сумма всех целых чисел от 100 до 500: {sum_100_to_500}")
a = int(input("Введите значение a (a < 500): "))
if a < 500:
    sum_a_to_500 = sum(range(a, 501))
    print(f"Сумма всех целых чисел от {a} до 500: {sum_a_to_500}")
else:
    print("Ошибка: a должно быть меньше 500.")
