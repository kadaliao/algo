#!/usr/bin/env python3
"""
归并排序算法

1) 将待排序区间分为子区间，排序好之后再合并。
2) 子区间递归1)过程
3) 区间只剩下1个元素时候停止（l == r)
"""


def merge_sort(a: list[int]):
    _merge_between(a, 0, len(a)-1)


def _merge_between(a: list[int], low: int, high: int):
    if low < high:
        mid = (low + high) // 2
        _merge_between(a, low, mid)
        _merge_between(a, mid+1, high)
        _merge(a, low, high, mid)


def _merge(a: list[int], low: int, high: int, mid: int):
    i, j = low, mid+1
    tmp = []
    while i <= mid and j <= high:
        if a[i] < a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end+1])
    a[low:high+1] = tmp


def test_merge_sort():
    a1 = [5, 2, 4, 1, 6, 0]
    merge_sort(a1)
    assert a1 == [0, 1, 2, 4, 5, 6]


    a2 = [1, 1, 1, 1]
    merge_sort(a2)
    assert a2 == [1, 1, 1, 1]

    a3 = []
    merge_sort(a3)
    assert a3 == []

    a4 = [4, 3, 2, 1, 0]
    merge_sort(a4)
    a4 = [0, 1, 2, 3, 4]

