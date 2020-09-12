#calculate number of fruits fallen within given range of house
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    app=orr=0

    for i in range (0,len(apples)):
        if a+apples[i]>=s and a+apples[i]<=t:
            app=app+1
    for i in range (0,len(oranges)):
        if b+oranges[i]>=s and b+oranges[i]<=t:
            orr=orr+1
    
    print(app)
    print(orr)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])

    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

