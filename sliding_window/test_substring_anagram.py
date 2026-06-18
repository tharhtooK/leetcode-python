import unittest

from sliding_window.substring_anagram import Solution

class TestSubstringAnagrams(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_1(self):
        self.assertEqual(self.sol.substring_anagram(s="caabab", t="aba"), 2)
    def test_2(self):
        self.assertEqual(self.sol.substring_anagram(s="cbaebabacd", t="abc"), 2)
    def test_3(self):
        self.assertEqual(self.sol.substring_anagram(s="abab", t="ab"), 3)

if __name__ == "__main__":
    unittest.main()