from willYou import solution

def test_willYou():
    assert solution(True, True, True) is False
    assert solution(True, False, True) is True
    assert solution(False, False, False) is False
    assert solution(False, False, True) is True