from arithmeticExpression import solution

def test_arithmeticExpression():
    assert solution(2, 3, 5) is True
    assert solution(8, 2, 4) is True
    assert solution(8, 3, 2) is False
    assert solution(6, 3, 3) is True
    assert solution(18, 2, 9) is True
    assert solution(2, 3, 6) is True
    assert solution(5, 2, 0) is False
    assert solution(10, 2, 2) is False
    assert solution(5, 2, 2) is False
    assert solution(1, 2, 1) is False
    assert solution(1, 2, 2) is True




