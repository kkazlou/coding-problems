import math

def solution(divisor, bound):
    x = math.floor(bound/divisor)
    return divisor * x