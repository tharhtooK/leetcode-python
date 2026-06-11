import unittest

class Solution:
    def __int__(self):
        pass

    def longest_substrings_with_unique_chars(self, s):
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
        left = right = 0
        hash_map = {}
        max_len = 0
        while right < len(s):
            while s[right] in hash_map and hash_map[s[right]] >= left:                
                left = hash_map[s[right]] + 1
            hash_map[s[right]] = right
            max_len = max(max_len, right-left+1)
            right += 1
        return max_len
