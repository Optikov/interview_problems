from math import sqrt
import time

def if_prime(a):
    b = 0
    for i in range(3, int(sqrt(a)) + 1, 2):     # Корень потому что если n = a * b, то min(a, b) <= sqrt(n)
        if a % i == 0:
            return False
    return True

start_time = time.time()
print(if_prime(67280421310721))
print("Time spent: %f seconds" % (time.time() - start_time))