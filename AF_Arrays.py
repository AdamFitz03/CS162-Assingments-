import numpy as np
import random
from numpy import dtype

def main():
    array = np.random.randint(0,99,(5,5),dtype=int) #5x5 array with random ints between 0 - 99
    total_sum = np.sum(array) #sums the numpy array using internal functions
    array_means = np.mean(array,axis=1)
    column_max = np.max(array,axis=0)


    print("_Randomly generated numpy array_")
    print(f"{array}\n")
    print(f"Row 2, column 3 has the value: {array[1,2]}\n")
    print(f"The total sum of the array is: {total_sum}\n")

    def means(x):
        row = 1
        for mean in x:
            print(f"The mean of row {row} is: {mean:.0f}")
            row += 1


    def maxes(y):
        column = 1
        for max in y:
            print(f"The maximum of column {column} is: {max}")
            column += 1

    means(array_means)
    print()
    maxes(column_max)

if __name__ == "__main__":
    main()
