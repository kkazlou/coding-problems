import pytest
from phoneCall import *

def test_centuryFromYear():
    assert solution(3, 1, 2, 20) == 14
    assert solution(2, 2, 1, 2) == 1
    assert solution(10, 1, 2, 22) == 11
    assert solution(2, 2, 1, 24) == 14
    assert solution(1, 2, 1, 6) == 3
    assert solution(10, 10, 10, 8) == 0