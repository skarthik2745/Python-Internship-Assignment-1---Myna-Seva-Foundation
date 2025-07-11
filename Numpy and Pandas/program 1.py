import numpy as np

arr = np.random.randint(1, 100, size=10)
even_count = np.sum(arr % 2 == 0)
odd_count = np.sum(arr % 2 != 0)
print("Array:", arr)
print("Even numbers:", even_count, "Odd numbers:", odd_count)