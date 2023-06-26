from maxMultiple import solution

def test_maxMultiple():
    assert solution(3, 10) == 9
    assert solution(2, 7) == 6
    assert solution(10, 50) == 50
    assert solution(7, 100) == 98
    assert solution(7, 20) == 14
    assert solution(5, 13) == 10
    assert solution(8, 88) == 88
    assert solution(10, 100) == 100
    assert solution(2, 5) == 4
    assert solution(3, 5) == 3
    assert solution(9, 11) == 9
    assert solution(8, 15) == 8
    assert solution(9, 60) == 54