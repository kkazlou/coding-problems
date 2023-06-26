from makeArrayConsecutive2 import solution

def test_makeArrayConsecutive2():
    assert solution([6, 2, 3, 8]) == 3
    assert solution([0, 3]) == 2
    assert solution([5, 4, 6]) == 0
    assert solution([6, 3]) == 2
    assert solution([1]) == 0