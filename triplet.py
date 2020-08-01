#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    if len(a)==len(b):
        ans=[0,0]
        l=len(a)
        for i in range(0,l):
            if a[i]>b[i]:
                ans[0]=ans[0]+1                
            if a[i]<b[i]:
                ans[1]=ans[1]+1
    return ans          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
