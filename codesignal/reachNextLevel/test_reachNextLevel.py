import pytest
from reachNextLevel import *

def test_reachNextLevel():
    assert solution(10, 15, 5) == True
    assert solution(10, 15, 4) == False
    assert solution(3, 6, 4) == True
    assert solution(84, 135, 36) == False
    assert solution(74, 170, 58) == False
    assert solution(80, 199, 15) == False
    assert solution(97, 57, 7) == True
    assert solution(235, 293, 4) == False