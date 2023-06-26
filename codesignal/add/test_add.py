from add import solution

def test_add():
    assert solution(1,2) == 3
    assert solution(0,1000) == 1000
    assert solution(2,-39) == -37
    assert solution(99,100) == 199