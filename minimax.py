#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max=0
    l=len(arr)
    min=arr[int(l/2)]
    s1=s2=0
    for i in range(0,l):
        if arr[i]<min:
            min=arr[i]
        if arr[i]>max:
            max=arr[i]

    f1=f2=1
    for j in range(0,l):
        s1=s1+arr[j]
        s2=s2+arr[j]
        if arr[j]==min and f1==1:
            s1=s1-arr[j]
            f1=0
        if arr[j]==max and f2==1:
            s2=s2-arr[j]
            f2=0

    print(s2,s1)
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
