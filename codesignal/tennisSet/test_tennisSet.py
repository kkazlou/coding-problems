from tennisSet import solution

def test_shapeArea():
    assert solution(3, 6) is True
    assert solution(8, 5) is False
    assert solution(6, 5) is False
    assert solution(7, 7) is False
    assert solution(6, 4) is True
    assert solution(7, 5) is True
    assert solution(3, 6) is True
    assert solution(7, 2) is False
    assert solution(7, 6) is True
    assert solution(4, 10) is False
    assert solution(0, 0) is False
