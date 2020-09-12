#The Utopian Tree goes through 2 cycles of growth every year following a specific pattern. How tall will that tree be after given number of growth cycles?
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    ans=1
    
    for i in range(1,n+1):
        if i%2==1:
            ans=ans*2
        elif i%2==0:
            ans=ans+1
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)
        fptr.write(str(result) + '\n')

    fptr.close()

