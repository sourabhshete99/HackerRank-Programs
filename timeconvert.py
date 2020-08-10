#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    f=0
    a1=int(s[0:2])
    
    if s[8:]=='PM':
        if a1<12:
            a1=a1+12
        if a1==12:
            a1=12
        a1=str(a1)
        f=f+1
    elif s[8:]=='AM':
        if a1==12:
            a1=str('00')
            f=f+1
    if f==0:
        a1=s[0:2]
    a2=s[3:5]
    a3=s[6:8]
    ans=a1+':'+a2+':'+a3
    return ans

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
