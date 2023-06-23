import pytest
from addTwoDigits import *

def test_addTwoDigits():
    assert solution(29) == 11
    assert solution(48) == 12
    assert solution(10) == 1
    assert solution(25) == 7
    assert solution(52) == 7
    assert solution(99) == 18
    assert solution(44) == 8
    assert solution(50) == 5
    assert solution(39) == 12
    assert solution(26) == 8