def solution(a, b):
    if a > b:
        return True
    # Is Odd Number
    elif (b - a)%2 == 1:
        return True
    else:
        return False