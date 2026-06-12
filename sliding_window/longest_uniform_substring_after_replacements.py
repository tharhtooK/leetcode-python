
"""
https://leetcode.com/problems/longest-repeating-character-replacement

"""


class Solution:
    def __int__(self):
        pass

    def longest_uniform_substring_after_replacements(self, s: str, k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(m)
        """
        max_len = 0
        left = right = 0
        highest_freq, num_of_char_to_replace = 0, 0
        char_freq_map = {}
        while right < len(s):
            freq = char_freq_map.get(s[right], 0) + 1
            char_freq_map[s[right]] = freq
            highest_freq = max(highest_freq, freq)            
            num_of_char_to_replace = right - left + 1 - highest_freq
            
            if num_of_char_to_replace > k:
                char_freq_map[s[left]] -= 1
                left += 1
            max_len = right - left + 1
            right += 1
        return max_len