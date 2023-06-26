from circleOfNumbers import solution

def test_circleOfNumbers():
    assert solution(10, 2) == 7
    assert solution(10, 7) == 2
    assert solution(4, 1) == 3
    assert solution(6, 3) == 0
    assert solution(18, 6) == 15
    assert solution(12, 10) == 4
    assert solution(18, 5) == 14