from killBit import solution

def test_killBit():
    assert solution(37, 3) == 33
    assert solution(37, 4) == 37
    assert solution(37, 2) == 37
    assert solution(0, 4) == 0
    assert solution(2147483647, 16) == 2147450879
    assert solution(374823748, 13) == 374819652
    assert solution(2734827, 4) == 2734819
    assert solution(1084197039, 15) == 1084197039
    assert solution(1160825071, 3) == 1160825067
    assert solution(2039063284, 4) == 2039063284
