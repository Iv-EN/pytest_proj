from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], -2, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice([1, 2, 3, 4], -3, -2) == [2]
    assert arrs.my_slice([1, 2, 3, 4], end=3) == [1, 2, 3]