from metroCard import solution

def test_metroCard():
    assert solution(30) == [31]
    assert solution(31) == [28, 30, 31]
