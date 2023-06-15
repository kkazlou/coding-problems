import pytest
from checkPalindrome import *

def test_checkPalindrome():
    assert solution("aabaa") == True
    assert solution("abac") == False
    assert solution("a") == True
    assert solution("abacaba") == True
    assert solution("hello") == False