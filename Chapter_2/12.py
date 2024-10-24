def k_to_b(kb):
    return kb * 1024
def b_to_k(bytes):
    return bytes / 1024
c = input("Введите 'k' для перевода из килобайтов в байты или 'b' для перевода из байтов в килобайты: ").strip().lower()
if c == 'k':
    kb = float(input("Введите количество килобайт: "))
    bytes = k_to_b(kb)
    print(f"{kb} килобайт = {bytes} байт")
elif c == 'b':
    bytes = float(input("Введите количество байт: "))
    kb = b_to_k(bytes)
    print(f"{bytes} байт = {kb} килобайт")
else:
    print("Неверно")

