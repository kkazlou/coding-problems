from knapsackLight import solution

def test_knapsackLight():
    assert solution(10, 5, 6, 4, 8) == 10
    assert solution(10, 5, 6, 4, 9) == 16
    assert solution(5, 3, 7, 4, 6) == 7
    assert solution(10, 2, 11, 3, 1) == 0
    assert solution(15, 2, 20, 3, 2) == 15
    assert solution(2, 5, 3, 4, 5) == 3
    assert solution(4, 3, 3, 4, 4) == 4
    assert solution(3, 5, 3, 8, 10) == 3
