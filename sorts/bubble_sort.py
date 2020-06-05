import unittest


def bubble_sort(a):
    length = len(a)
    if length <= 1:
        return

    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            return


def bubble_sort_adv(seq, cmp_key=lambda x: x):
    length = len(seq)
    if length <= 1:
        return
    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if cmp_key(seq[j]) > cmp_key(seq[j + 1]):
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                swapped = True
        if not swapped:
            return


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        test_array = []
        bubble_sort(test_array)
        self.assertEqual(test_array, [])

        test_array = [1]
        bubble_sort(test_array)
        self.assertEqual(test_array, [1])

        test_array = [1, 1, 1, 1]
        bubble_sort(test_array)
        self.assertEqual(test_array, [1, 1, 1, 1])

        test_array = [4, 1, 2, 3]
        bubble_sort(test_array)
        self.assertEqual(test_array, [1, 2, 3, 4])

        test_array = [4, 3, 2, 3]
        bubble_sort(test_array)
        self.assertEqual(test_array, [2, 3, 3, 4])

    def test_bubble_sort_adv(self):
        from operator import itemgetter, attrgetter
        from collections import namedtuple
        from copy import copy

        Student = namedtuple('Student', 'name age')
        stus = [
            Student('Kada', 28),
            Student('Kada', 24),
            Student('Linny', 25),
            Student('Aitong', 23),
            Student('Neo', 25),
        ]

        bubble_sort_adv(stus)
        self.assertEqual(stus, [
            Student('Aitong', 23),
            Student('Kada', 24),
            Student('Kada', 28),
            Student('Linny', 25),
            Student('Neo', 25)
        ])

        by_age = itemgetter(1)
        by_name = attrgetter('name')

        stus = [
            Student('Kada', 28),
            Student('Kada', 24),
            Student('Linny', 25),
            Student('Aitong', 23),
            Student('Neo', 25)
        ]

        bubble_sort_adv(stus, by_name)
        bubble_sort_adv(stus, by_age)
        self.assertEqual(stus, [
            Student('Aitong', 23),
            Student('Kada', 24),
            Student('Linny', 25),
            Student('Neo', 25),
            Student('Kada', 28),
        ])


if __name__ == "__main__":
    unittest.main()
