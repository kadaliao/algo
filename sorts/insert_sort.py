#!/usr/bin/env python3
"""
插入排序

1）从未排序区间选择第一个元素
2）依次从后往前与已排序区间进行比较，并向后移动元素
3）插入到合适的已排序位置，对剩余区间进行1）操作
"""


def insert_sort(a: list[int]):
    n = len(a)

    for i in range(1, n):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x


def test_insert_sort():
    a = [6, 1, 0, -1, 2, 4, 5, 3]
    insert_sort(a)
    assert a == [-1, 0, 1, 2, 3, 4, 5, 6]

    a = []
    insert_sort(a)
    assert a == []

    a = [1, 1, 1, 1]
    insert_sort(a)
    assert a == [1, 1, 1, 1]

    a = [4, 3, 2, 1]
    insert_sort(a)
    assert a == [1, 2, 3, 4]
