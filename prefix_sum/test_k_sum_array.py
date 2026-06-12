import unittest

from prefix_sum.k_sum_array import Solution


class TestKSumSubarray(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_1(self):
        self.assertEqual(self.sol.k_sum_subarray([1, 2, -1, 1, 2], k=3), 3)

if __name__ == "__main__":
    unittest.main()