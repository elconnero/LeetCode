#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getRemovableIndices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#

def getRemovableIndices(str1, str2):
    
    for i, char in enumerate(str1):
        
        if char == str2[i]: continue
        else: 
            str1 = str1[:i] + str1[i+1:]
            break

    if str1 == str2: return str1
    else: return [-1]

def main():
    print(getRemovableIndices("abdgggda", "abdggda"))  # expected [3, 4, 5]
    print(getRemovableIndices("abcd", "acd"))           # expected [1]
    print(getRemovableIndices("abcd", "abd"))           # expected [2]
    print(getRemovableIndices("abcd", "abc"))           # expected [3]
    print(getRemovableIndices("ab", "a"))               # expected [1]
    


if __name__ == '__main__':
    str1 = input()

    str2 = input()

    result = getRemovableIndices(str1, str2)

    print('\n'.join(map(str, result)))


