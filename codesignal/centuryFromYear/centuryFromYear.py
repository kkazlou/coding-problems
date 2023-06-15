# https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN

# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100,
# the second - from the year 101 up to and including the year 200, etc.

import math

def solution(year):
    
    rest = year%100

    if rest == 0:
        return year/100
    else:
        return math.floor(year/100) + 1

print(solution(1905))
