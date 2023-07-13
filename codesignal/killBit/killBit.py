def solution(n, k):
    return killBit(n, k)

def killBit(n, k):

    binary_str = format(n, 'b')
    binary_arr = list(binary_str)

    try:
        binary_arr[-k] = '0'
    except Exception as e:
        print(f"Exception - {e}")

    result = ''.join(binary_arr)

    return int(result, 2)