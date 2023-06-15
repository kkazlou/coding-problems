import math

def solution(year):
    
    rest = year%100

    if rest == 0:
        return year/100
    else:
        return math.floor(year/100) + 1

print(solution(1905))
