#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    l=int(len(arr))
    s=''
    for i in range(0,l):
        s=s+str(arr[l-1-i])
        s=s+' '

    print(s)
	