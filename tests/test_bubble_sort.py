import unittest
from methods.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_case1(self):
        arr = [64, 34, 25, 12, 22, 11, 63]
        result = bubble_sort(arr)
        expected = [11, 12, 22, 25, 34, 63, 64]
        self.assertEqual(arr, [11, 12, 22, 25, 34, 63, 64])

if __name__ == '__main__':
    unittest.main()
