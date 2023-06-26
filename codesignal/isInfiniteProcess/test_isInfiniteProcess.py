from isInfiniteProcess import solution

def test_isInfiniteProcess():
    assert solution(2, 6) is False
    assert solution(2, 3) is True
    assert solution(2, 10) is False
    assert solution(0, 1) is True
    assert solution(3, 1) is True
    assert solution(10, 10) is False
    assert solution(5, 10) is True
    assert solution(6, 10) is False
    assert solution(10, 0) is True
    assert solution(5, 5) is False