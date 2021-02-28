#!/usr/bin/env python3
"""
快速排序

(1) 处理整个区间，以最后一个位置为pivot
(2) 分区函数找到点q，使得q之前都比pivot小，q之后都比pivot大
(3) 用(1)递归处理q之前的区间、q之后的区间
(4) 区间长度为1时候退出（l==r）
"""


def quick_sort(a: list[int]):
    quick_sort_between(a, 0, len(a) - 1)


def quick_sort_between(a: list[int], l: int, r: int):
    if l < r:
        q = partition(a, l, r)
        quick_sort_between(a, l, q - 1)
        quick_sort_between(a, q + 1, r)


# def partition(a: list[int], l: int, r: int) -> int:
#     pivot = a[r]
#     i, j = l, r
#     while i < j:
#         while a[i] <= pivot and i < r:
#             i += 1
#         while a[j] >= pivot and j > i:
#             j -= 1
#         a[i], a[j] = a[j], a[i]
#     a[i], a[r] = a[r], a[i]
#     return i


def partition(a: list[int], l: int, r: int) -> int:
    pivot, p = a[r], l
    # p指向第一个大于pivot的位置
    for i in range(l, r):
        # 每遇到一个小于等于pivot的数，就交换到p的位置
        # p后移，使得p之前都小于等于pivot
        if a[i] <= pivot:
            a[i], a[p] = a[p], a[i]
            p += 1
    # pivot换到p位置，满足p位置之前小于等于pivot
    a[r], a[p] = a[p], a[r]
    return p


def test_merge_sort():
    a1 = [5, 2, 4, 1, 6, 0]
    quick_sort(a1)
    assert a1 == [0, 1, 2, 4, 5, 6]

    a2 = [1, 1, 1, 1]
    quick_sort(a2)
    assert a2 == [1, 1, 1, 1]

    a3 = []
    quick_sort(a3)
    assert a3 == []

    a4 = [4, 3, 2, 1, 0]
    quick_sort(a4)
    a4 = [0, 1, 2, 3, 4]
