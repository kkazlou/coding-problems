from arrayPacking import solution1
from arrayPacking import solution2

def test_arrayPacking_solution1():
    assert solution1([24, 85, 0]) == 21784
    assert solution1([23, 45, 39]) == 2567447
    assert solution1([1, 2, 4, 8]) == 134480385
    assert solution1([5]) == 5
    assert solution1([187, 99, 42, 43]) == 724198331

def test_arrayPacking_solution2():
    assert solution2([24, 85, 0]) == 21784
    assert solution2([23, 45, 39]) == 2567447
    assert solution2([1, 2, 4, 8]) == 134480385
    assert solution2([5]) == 5
    assert solution2([187, 99, 42, 43]) == 724198331
