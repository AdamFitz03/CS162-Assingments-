import numpy as np
from numpy import dtype
import random

""" Program using numpy and random to generate a 5 x 5 array with integers ranging from 
    0-99, this array will be unique every time the script is ran. It then uses built in 
    functions to evaluate the sum of the array, mean of each row, and max of each column, 
    then prints the results before proceeding to the functions below."""

array = np.random.randint(0,99,(5,5),dtype=int) #dtype sets the data created in the array to be integers.
total_sum = np.sum(array)
array_means = np.mean(array,axis=1) #axis 1 allows rows
column_max = np.max(array,axis=0) #axis 0 allows columns

print("\n_Randomly generated numpy array_")
print(f"{array}\n")
print(f"Row 2, Column 3 has the value: {array[1,2]}\n")
print(f"The total sum of the array = {total_sum}\n")

def means(x):
    """ Function that takes the means stored in array_means as input, then
        it uses a for loop to iterate through each of the means and prints
        out a nice clean output for each. """
    row = 1
    for mean in x:
        print(f"The mean of row {row} is: {mean:.0f}")
        row += 1


def maxes(y):
    """ Function that works exactly the same as the means function above,
        only it is using the max values stored in column_maxes instead. """
    column = 1
    for max in y:
        print(f"The maximum of column {column} is: {max}")
        column += 1


if __name__ == "__main__":
    means(array_means)
    print()
    maxes(column_max)