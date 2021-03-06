#!/usr/bin/env python3

"""
动态数组特性实现的队列

1）从head出，tail入
2）tail到最后位，数组却没满，向前搬动数据
"""

from typing import Optional


class DyanmicArrayQueue:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._items = []
        self._head = 0
        self._tail = 0

    def enque(self, val: int) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            self._items[0 : self._tail] = self._items[self._head : self._tail]
            self._tail = self._tail - self._head
            self._head = 0

        self._items.insert(self._tail, val)
        self._tail += 1
        return True

    def deque(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item

    def __repr__(self):
        return f"<DynamicArrayQueue {self._items}>"

    def __str__(self):
        return f"{self._items[self._head:self._tail]}"


def test_enque():
    q = DyanmicArrayQueue(5)

    q.enque(1)
    q.enque(2)
    q.enque(3)
    q.enque(4)
    q.enque(5)

    assert str(q) == str([1, 2, 3, 4, 5])
    assert not q.enque(6)
    assert str(q) == str([1, 2, 3, 4, 5])


def test_deque():
    q = DyanmicArrayQueue(5)

    assert q.deque() is None
    q.enque(1)
    q.enque(2)
    q.enque(3)
    assert q.deque() == 1
    assert q.deque() == 2
    assert q.deque() == 3

    assert q.deque() is None
