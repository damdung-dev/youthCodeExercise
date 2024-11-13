import numpy as np

def print_multiplication_table():
    for i in range(1, 11):
        for j in range(2, 10):
            print(f"{j} x {i} = {j*i}", end='\t')
        print()

print_multiplication_table()
