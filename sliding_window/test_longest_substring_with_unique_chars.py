import unittest

from sliding_window.longest_substring_with_unique_chars import Solution


class TestLongestSubstringsWithUniqueChars(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_1(self):
        self.assertEqual(self.sol.longest_substrings_with_unique_chars("abcba"), 3)
    def test_2(self):
        self.assertEqual(self.sol.longest_substrings_with_unique_chars("cabcdeca"), 5)
    def test_3(self):
        self.assertEqual(self.sol.longest_substrings_with_unique_chars_optimized("abcba"), 3)
    def test_4(self):
        self.assertEqual(self.sol.longest_substrings_with_unique_chars_optimized("cabcdeca"), 5)
    def test_5(self):
        self.assertEqual(self.sol.longest_substrings_with_unique_chars("abcabcbb"), 3)
    def test_6(self):
        self.assertEqual(self.sol.longest_substrings_with_unique_chars_optimized("abcabcbb"), 3)
    def test_7(self):
        self.assertEqual(self.sol.longest_substrings_with_unique_chars("bbbbb"), 1)
    def test_8(self):
        self.assertEqual(self.sol.longest_substrings_with_unique_chars_optimized("bbbbb"), 1)
    def test_9(self):
        self.assertEqual(self.sol.longest_substrings_with_unique_chars("pwwkew"), 3)
    def test_10(self):
        self.assertEqual(self.sol.longest_substrings_with_unique_chars_optimized("pwwkew"), 3)

if __name__ == "__main__":
    unittest.main()