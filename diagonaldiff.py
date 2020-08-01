#!/bin/python3. Given a matrix, calc the difference between the diagonal elements

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    l=len(arr)
    d1=d2=0
    for j in range (0,l):
        d1=d1+arr[j][j]
        d2=d2+arr[j][l-1-j]

    if d1>=d2:
        ans=d1-d2
    else:
        ans=d2-d1
    return ans

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
