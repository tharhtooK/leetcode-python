from typing import List
import unittest

class Solution:
    def __init__(self):
        pass

    def shift_zeros_to_the_end(self, nums: List[int]):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        first = 0
        for second in range(len(nums)):
            if nums[second] != 0:
                nums[first], nums[second] = nums[second], nums[first]
                first += 1
        return nums

