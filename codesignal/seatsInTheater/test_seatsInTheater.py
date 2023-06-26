from seatsInTheater import solution

def test_seatsInTheater():
    assert solution(16, 11, 5, 3) == 96
    assert solution(1, 1, 1, 1) == 0
    assert solution(13, 6, 8, 3) == 18
    assert solution(60, 100, 60, 1) == 99
    assert solution(1000, 1000, 1000, 1000) == 0