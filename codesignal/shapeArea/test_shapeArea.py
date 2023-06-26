from shapeArea import solution

def test_shapeArea():
    assert solution(2) == 5
    assert solution(3) == 13
    assert solution(1) == 1
    assert solution(5) == 41
    assert solution(7000) == 97986001
    assert solution(8000) == 127984001
    assert solution(9999) == 199940005