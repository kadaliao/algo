#!/usr/bin/env python3
"""
选择排序

每次从未排序区间选择一个最小的数，加到已排序区间后面
"""


def select_sort(a: list[int]):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[min_index], a[i] = a[i], a[min_index]


def test_select_sort():
    a = [-1, 0, 1, 5, 4, 2, 3]
    select_sort(a)
    assert a == [-1, 0, 1, 2, 3, 4, 5]

    a = [1, 1, 1, 1]
    select_sort(a)
    assert a == [1, 1, 1, 1]

    a = [4, 3, 2, 1]
    select_sort(a)
    assert a == [1, 2, 3, 4]

    a = []
    select_sort(a)
    assert a == []
