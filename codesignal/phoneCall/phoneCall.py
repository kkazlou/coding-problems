def solution(min1, min2_10, min11, s):
    count = 0
    while s >= 0:
        # min1
        if count == 0:
            if s - min1 >= 0:
                s -= min1
                count += 1
            else:
                break
        # min2_10
        elif count in range(1,10):
            if s - min2_10 >= 0:
                s -= min2_10
                count += 1
            else:
                break
        # min11
        else:
            if s - min11 >= 0:
                s -= min11
                count += 1
            else:
                break
    return count