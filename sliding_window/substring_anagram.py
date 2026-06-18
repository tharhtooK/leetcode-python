class Solution:
    def __int__(self):
        pass

    def substring_anagram(self, s: str, t: str) -> int:
        """
        Anagram -> can check against frequencies of the characters

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count =0
        first = second = 0
        expected_freqs = [0] * 26
        freqs = [0] * 26
        for c in t:
            expected_freqs[ord(c) - ord('a')] += 1
        
        while second < len(s):
            freqs[ord(s[second]) - ord('a')] += 1
            
            if second - first + 1 == len(t):
                if freqs == expected_freqs:
                    count += 1
                freqs[ord(s[first]) - ord('a')] -= 1
                first += 1
            second += 1
        return count