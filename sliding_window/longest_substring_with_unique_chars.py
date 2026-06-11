import unittest

"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

- dynamic sliding window

- within each window, we want to keep unique characters, if duplicates found, adjust the window to remove the dups

"""

class Solution:
    def __int__(self):
        pass

    def longest_substrings_with_unique_chars(self, s):
        """
        Time Complexity: O(n) -> iter thru given string length
        Space Complexity: O(m) => store the unique char in hashset

        """
        left = right = 0
        hash_set = set()
        max_len = 0
        while right < len(s):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            hash_set.add(s[right])
            max_len = max(max_len, right-left+1)
            right += 1
        return max_len

    def longest_substrings_with_unique_chars_optimized(self, s):
        """
        Time Complexity: O(n) -> iter thru given string length
        Space Complexity: O(m) => store the unique char in hashmap

        """
        left = right = 0
        prev_indexes = {}
        max_len = 0
        while right < len(s):
            while s[right] in prev_indexes and prev_indexes[s[right]] >= left:                
                left = prev_indexes[s[right]] + 1
            prev_indexes[s[right]] = right
            max_len = max(max_len, right-left+1)
            right += 1
        return max_len
