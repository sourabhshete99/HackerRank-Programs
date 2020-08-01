#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    l=len(ar)
    max=0
    for i in range(0,l):
        if ar[i]>max:
            max=ar[i]
    cnt=0
    for i in range(0,l):
        if ar[i]==max:
            cnt=cnt+1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
