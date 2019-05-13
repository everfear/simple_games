import random as r
import time

symbols = ["0", "1", "", ""]
line = []
counter = 0

# первая линия
# 118 в ширину
for i in range(218):
    x = r.randint(0, 3)
    line.append(symbols[x])
    counter += 1

# 10000 в длину
# меняем по 10 цифр каждый 5 раз
for i in range(10000):
    if counter % 5 == 0:
        r_symbols = [r.randint(0, 117) for x in range(10)]

        for i in r_symbols:
            line[i] = symbols[r.randint(0, 3)]

    print(*line)
    counter += 1
    time.sleep(0.01)    # пауза на 0.01 сек каждый проход
