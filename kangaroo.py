#given two kangaroos position and speed, find out whether they meet at a common point or not
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    y='YES'
    n='NO'

    if x1<x2 and v1<v2:  
        return n
    
    else:
        a=0+x1
        b=0+x2
        for i in range(0, x1+v1+x2+v2):
            a=a+v1
            b=b+v2
            if a==b:
                return y        
        return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')
    fptr.close()

