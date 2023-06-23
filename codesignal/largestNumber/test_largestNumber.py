import pytest
from largestNumber import *

def test_largestNumber():
    assert solution(2) == 99
    assert solution(1) == 9
    assert solution(7) == 9999999
    assert solution(4) == 9999
    assert solution(3) == 999
    