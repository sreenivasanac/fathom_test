#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'changedSort' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def getSmallestChar(s, freq, prev_char):
    for char in sorted(freq.keys()):
        if freq[char] > 0 and char > prev_char:
            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]
            return char
    return -1

def getLargestChar(s, freq, prev_char):
    for char in reversed(sorted(freq.keys())):
        if freq[char] > 0 and char < prev_char:
            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]
            return char
    return -1

def changedSort(s):
    # Write your code here
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    output = ""

    while(len(output) != len(s)):
        prev_char = getSmallestChar(s, freq, "_")
        output += str(prev_char)

        while(prev_char != -1):
            prev_char = getSmallestChar(s, freq, prev_char)
            # print(prev_char)
            if prev_char != -1:
                output += str(prev_char)

        # print(output + str(" after getSmallestChar"))

        prev_char = "}"
        while(prev_char != -1):
            prev_char = getLargestChar(s, freq, prev_char)
            # print(prev_char)
            if prev_char != -1:
                output += str(prev_char)

    return output

print(changedSort("abbcyxc"))
