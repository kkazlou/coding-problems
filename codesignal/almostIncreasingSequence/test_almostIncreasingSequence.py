from almostIncreasingSequence import solution

def test_almostIncreasingSequence():
    assert solution([1, 3, 2, 1]) is False
    assert solution([1, 3, 2]) is True
    assert solution([1, 2, 1, 2]) is False
    assert solution([3, 6, 5, 8, 10, 20, 15]) is False
    assert solution([1, 1, 2, 3, 4, 4]) is False
    assert solution([1, 4, 10, 4, 2]) is False
    assert solution([10, 1, 2, 3, 4, 5]) is True
    assert solution([1, 1, 1, 2, 3]) is False
    assert solution([0, -2, 5, 6]) is True
    assert solution([1, 2, 3, 4, 5, 3, 5, 6]) is False
    assert solution([40, 50, 60, 10, 20, 30]) is False
    assert solution([1, 1]) is True
    assert solution([1, 2, 5, 3, 5]) is True
    assert solution([1, 2, 5, 5, 5]) is False
    assert solution([10, 1, 2, 3, 4, 5, 6, 1]) is False
    assert solution([1, 2, 3, 4, 3, 6]) is True
    assert solution([1, 2, 3, 4, 99, 5, 6]) is True
    assert solution([123, -17, -5, 1, 2, 3, 12, 43, 45]) is True
    assert solution([3, 5, 67, 98, 3]) is True


