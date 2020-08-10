#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    l=int(len(grades))
    for i in range(0,l):
        if(grades[i]>=38):
            rem=int(grades[i]%5)
            if(rem>=3):
                print(grades[i]+5-rem)
            else:
                print(grades[i])

        else:
            print(grades[i])

