import pytest
from arithmeticExpression import *

def test_arithmeticExpression():
    assert solution(2, 3, 5) == True
    assert solution(8, 2, 4) == True
    assert solution(8, 3, 2) == False
    assert solution(6, 3, 3) == True
    assert solution(18, 2, 9) == True
    assert solution(2, 3, 6) == True
    assert solution(5, 2, 0) == False
    assert solution(10, 2, 2) == False
    assert solution(5, 2, 2) == False
    assert solution(1, 2, 1) == False
    assert solution(1, 2, 2) == True




