#!/usr/bin/env python3

from typing import Optional


class CircularQueue:
    def __init__(self, capacity: int = 10):
        self._capacity = capacity + 1
        self._items = [None] * self._capacity
        self._head = 0
        self._tail = 0

    @property
    def capacity(self) -> int:
        return self._capacity - 1

    def is_empty(self) -> bool:
        return self._tail == self._head

    def is_full(self) -> bool:
        return (self._tail + 1) % self._capacity == self._head

    def enqueue(self, val: int) -> bool:
        if self.is_full():
            return False
        self._items[self._tail] = val
        self._tail = (self._tail + 1) % self._capacity
        return True

    def dequeue(self) -> Optional[int]:
        if self.is_empty():
            return None
        item = self._items[self._head]
        self._head = (self._head + 1) % self._capacity
        return item

    def __str__(self):
        return f"{list(item for item in self._items[self._head:self._tail])}"

    def __repr__(self):
        return f"<CircularQueue items: {self._items}, capacity: {self._capacity}, head: {self._head}, tail: {self._tail}>"


def test_circular_queue():
    q = CircularQueue(10)
    assert q.capacity == 10
    assert q.is_empty()
    assert q.dequeue() is None

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(0)

    assert q.dequeue() == 1
    assert q.dequeue() == 2

    for i in range(1, 10):
        assert q.enqueue(i)

    assert q.is_full()
    assert not q.enqueue(10)
