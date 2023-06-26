from adjacentElementsProduct import solution

def test_adjacentElementsProduct():
    assert solution([3, 6, -2, -5, 7, 3]) == 21
    assert solution([-1, -2]) == 2
    assert solution([5, 1, 2, 3, 1, 4]) == 6
    assert solution([1, 2, 3, 0]) == 6
    assert solution([9, 5, 10, 2, 24, -1, -48]) == 50