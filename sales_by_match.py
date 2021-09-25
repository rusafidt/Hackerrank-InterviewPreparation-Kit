import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    ar.sort()
    a = 0
        while(len(ar) > 1):
        if(ar[0]==ar[1]):
            a+=1
            del(ar[:2])
        else:
            del(ar[0])
    return (a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)