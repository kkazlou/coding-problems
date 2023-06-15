import pytest
from centuryFromYear import *

def test_centuryFromYear():
    assert solution(1905) == 20
    assert solution(1700) == 17
    assert solution(1988) == 20
    assert solution(2000) == 20