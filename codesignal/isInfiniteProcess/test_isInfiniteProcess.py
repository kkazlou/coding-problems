import pytest
from isInfiniteProcess import *

def test_isInfiniteProcess():
    assert solution(2, 6) == False
    assert solution(2, 3) == True
    assert solution(2, 10) == False
    assert solution(0, 1) == True
    assert solution(3, 1) == True
    assert solution(10, 10) == False
    assert solution(5, 10) == True
    assert solution(6, 10) == False
    assert solution(10, 0) == True
    assert solution(5, 5) == False