#!/bin/python3

import math
import os
import random
import re
import sys

# Loop CAN'T be too long (like when n equals 1000000) because it causes timeout.
# My solution to this was avoiding a big loop counting the a's for the whole word, then
# multiply it by how many times the word will be repeated. After that, I use the loop to count the a's
# when the word is partitionated.
def repeatedString(s, n):
    a = math.floor(n/len(s)) * s.count('a')
    cnt = n%len(s)
    l = list(s)

    for i in range(cnt):
        if(l[i] == 'a'):
            a += 1;

    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

#https://www.hackerrank.com/challenges/repeated-string/
