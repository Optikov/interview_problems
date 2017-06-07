from __future__ import print_function
import random

"""
Q: Какова вероятность, что оба приятеля окажутся на соседних местах за круглым столом на восемь человек?
A: Вероятность, что один из приятелей окажется по левую или правую руку - 1/7 (семь возможных вариантов)
Осталось 6 мест - и только одно из них годится для нашего случая - одно из шести - 1/6
Выходит что совпадение будет только - учитывая, что годится два варианта (когда первый приятиель слева, а второй - справа и наоборот) -
в 2/(7*6) то есть в 2/42  ~ 0.0476. 

Програмка на Python, иллюстрирующая, что происходит "экспериментально".
"""

PROBABILITY = 0.5
N = 1000000

print("Starting")
wins = 0
for i in range(0, N):
    A = random.randint(1, 7)
    B = A
    while A == B:
        B = random.randint(1, 7)


    if (A == 1 and B == 7) or (A == 7 and B == 1):
        wins = wins + 1



print(wins, "out of",  N)
print("And probability being %f" % (1.0 * wins / N))
print("which must be close to 2/42 ~ %f" % (2.0 / 42))
