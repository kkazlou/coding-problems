from candies import solution

def test_candies():
    assert solution(3, 10) == 9
    assert solution(1, 2) == 2
    assert solution(4, 4) == 4
    assert solution(4, 15) == 12
    assert solution(9, 100) == 99
    assert solution(8, 2) == 0
    assert solution(3, 3) == 3
    assert solution(7, 10) == 7
    assert solution(3, 23) == 21
