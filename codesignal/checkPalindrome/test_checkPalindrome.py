from checkPalindrome import solution

def test_checkPalindrome():
    assert solution("aabaa") is True
    assert solution("abac") is False
    assert solution("a") is True
    assert solution("abacaba") is True
    assert solution("hello") is False