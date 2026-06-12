import unittest

from sliding_window.longest_uniform_substring_after_replacements import Solution


class TestLongestUniformSubstringAfterReplacements(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_1(self):
        self.assertEqual(self.sol.longest_uniform_substring_after_replacements("aabcdcca", 2), 5)
    def test_2(self):
        self.assertEqual(self.sol.longest_uniform_substring_after_replacements("abab", 2), 4)
    def test_3(self):
        self.assertEqual(self.sol.longest_uniform_substring_after_replacements("AABABBA", 1), 4)
    def test_4(self):
        s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
        self.assertEqual(self.sol.longest_uniform_substring_after_replacements(s, 4), 7)

if __name__ == "__main__":
    unittest.main()