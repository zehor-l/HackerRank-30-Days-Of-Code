#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numSwaps = 0
for i in range(n):
    for j in range(n-1):
        if(a[j] > a[j+1]):
            numSwaps+=1
            a[j], a[j+1] = a[j+1], a[j]
    if(numSwaps is 0):
        break
print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n-1]))
    
