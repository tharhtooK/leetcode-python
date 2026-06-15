import unittest

from binary_search.find_insertion_index import Solution


class TestFindInsertionIndex(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_1(self):
        self.assertEqual(self.sol.find_the_insertion_index([1, 2, 4, 5, 7, 8, 9], 4), 2)
    def test_2(self):
        self.assertEqual(self.sol.find_the_insertion_index([1, 2, 4, 5, 7, 8, 9], 6), 4)
    def test_3(self):
        self.assertEqual(self.sol.find_the_insertion_index([1,3,5,6], 5), 2)
    def test_4(self):
        self.assertEqual(self.sol.find_the_insertion_index([1,3,5,6], 2), 1)
    def test_5(self):
        self.assertEqual(self.sol.find_the_insertion_index([1,3,5,6], 7), 4)
    def test_6(self):
        self.assertEqual(self.sol.find_the_insertion_index([1], 0), 0)
    
if __name__ == "__main__":
    unittest.main()