from extraNumber import solution

def test_extraNumber():
    assert solution(2, 7, 2) == 7
    assert solution(3, 2, 3) == 2
    assert solution(5, 5, 1) == 1
    assert solution(500000000, 3, 500000000) == 3
    assert solution(1, 5, 1) == 5
    assert solution(5, 5, 3) == 3
    assert solution(5, 1, 1) == 5
    assert solution(4000000, 3000000, 4000000) == 3000000
    assert solution(469992838, 66019520, 66019520) == 469992838
    assert solution(1, 1, 1) == 1