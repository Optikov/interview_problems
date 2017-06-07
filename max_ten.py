"""
Поиск десяти максимальных элементов в массиве
"""

import numpy as np
MAX_INT = 1000
NUMBER_OF_ITEMS = 100
arr = np.random.randint(0, MAX_INT, NUMBER_OF_ITEMS)

def max_ten(arr):
    max_ten_values = np.copy(arr[0:10])


    for x in arr[10:]:
        if x > min(max_ten_values):                         # Если x вошёл в рейтинг hot10, то есть опередил хотя бы одного входящего
            max_ten_values[np.argmin(max_ten_values)] = x   # туда, то занимающий последнее место точно должен покинуть рейтинг.
    return max_ten_values




print("Array: ", arr, "\n")
print("max ten found with our algorithm:")
print(sorted(max_ten(arr)), "\n")

print("and using built-in functions:")
print(sorted(arr)[-10:])
