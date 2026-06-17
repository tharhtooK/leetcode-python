import unittest

from two_pointers.shift_zeros_to_the_end import Solution


class TestShiftZerosToTheEnd(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_1(self):
        self.assertListEqual(self.sol.shift_zeros_to_the_end([0, 1, 0, 3, 2]), [1, 3, 2, 0, 0])
    def test_2(self):
        self.assertListEqual(self.sol.shift_zeros_to_the_end([1,0]), [1, 0])
    def test_3(self):
        self.assertListEqual(self.sol.shift_zeros_to_the_end([1,0,1]), [1, 1,0])
    def test_4(self):
        self.assertListEqual(self.sol.shift_zeros_to_the_end([0,1,0,3,12]), [1,3,12,0,0])

if __name__ == "__main__":
    unittest.main()