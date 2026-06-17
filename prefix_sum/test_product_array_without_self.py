import unittest

from prefix_sum.product_array_without_self import Solution

class TestProductArrayWithoutSelf(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_1(self):
        self.assertEqual(self.sol.product_array_without_self([2, 3, 1, 4, 5]), [60, 40, 120, 30, 24])

if __name__ == "__main__":
    unittest.main()