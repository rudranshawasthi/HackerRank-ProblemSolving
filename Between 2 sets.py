#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    fact = list()
    x = min(b)
    flg = 0
    for i in range(1,x+1):
        for j in b:
            if j%i != 0:
                flg = 1
                break
        if flg == 0:
            fact.append(i)
        flg = 0
    x = 0
    while x < len( fact ):
        for j in a:
            if fact[x] % j != 0:
                fact.remove(fact[x])
                x -= 1
                break
        x += 1
    print(len(fact))


if __name__ == '__main__':
    arr = list( map( int, input().rstrip().split() ) )

    brr = list( map( int, input().rstrip().split() ) )

    total = getTotalX( arr, brr )

