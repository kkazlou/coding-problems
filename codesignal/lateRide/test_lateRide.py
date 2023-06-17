import pytest
from lateRide import *

def test_lateRide():
    assert solution(240) == 4
    assert solution(808) == 14
    assert solution(1439) == 19
    assert solution(0) == 0
    assert solution(23) == 5
    assert solution(8) == 8