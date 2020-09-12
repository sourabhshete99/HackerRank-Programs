#group the given matrix into groups of 3*3 and calc the highest total made by elements

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    l=len(arr)
    max=-54
    for i in range(0,4):
        for j in range(0,4):
            sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if sum>=max:
                max=sum

    print(max)

