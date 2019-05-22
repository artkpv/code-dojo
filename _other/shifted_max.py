import unittest


def find_max(numbers):
    if not numbers:
        return None  # FIX

    left = 0
    right = len(numbers)-1  # MISTYPO
    if numbers[left] == numbers[right]:
        return numbers[left]
    while left < right:
        mid = (right + left)//2
        if mid + 1 <= right:
            if numbers[mid] > numbers[mid+1]:
                return numbers[mid]
        elif min - 1 >= left:
            if numbers[mid-1] > numbers[mid]:
                return numbers[mid-1]
        if numbers[left] < numbers[right]:
            return numbers[right]
        elif numbers[mid] < numbers[left]:
            right = mid-1
        else:
            left = mid
    return numbers[left]


class Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(find_max([1]), 1)

    def test_empty(self):
        self.assertEqual(find_max([]), None)

    def test_ten_elements(self):
        self.assertEqual(find_max([7,8,9,1,2,3,4,5,6]), 9)

    def test_ten_elements_max_at_right(self):
        self.assertEqual(find_max([3,4,5,6,7,8,9,1,2]), 9)

    def test_no_shift(self):
        self.assertEqual(find_max([1,2,3,4,5,6,7,8,9]), 9)


unittest.main()
