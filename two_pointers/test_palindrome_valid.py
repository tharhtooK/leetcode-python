import unittest

from two_pointers.palindrome_valid import Solution


class TestPalindromeValid(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_1(self):
        self.assertEqual(self.sol.is_palindrome_valid("a dog! a panic in a pagoda"), True)
    def test_2(self):
        self.assertEqual(self.sol.is_palindrome_valid("racecar"), True)
    
if __name__ == "__main__":
    unittest.main()