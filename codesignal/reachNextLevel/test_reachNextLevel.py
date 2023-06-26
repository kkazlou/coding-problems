from reachNextLevel import solution

def test_reachNextLevel():
    assert solution(10, 15, 5) is True
    assert solution(10, 15, 4) is False
    assert solution(3, 6, 4) is True
    assert solution(84, 135, 36) is False
    assert solution(74, 170, 58) is False
    assert solution(80, 199, 15) is False
    assert solution(97, 57, 7) is True
    assert solution(235, 293, 4) is False