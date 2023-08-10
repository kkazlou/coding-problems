def solution1(a):
    result = ''
    for i in a[::-1]:
        result += format(i, 'b').zfill(8)
    return int(result, 2)


def solution2(a):
    result = 0
    for i in range(len(a)):
        result += a[i] << 8*i
    return result
