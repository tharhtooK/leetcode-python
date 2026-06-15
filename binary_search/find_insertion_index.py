from typing import List


class Solution:
    def __init__(self):
        pass

    def find_the_insertion_index(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(log(n)) -> over n+1 array
        Space Complexity: O(1)
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= k:
                right = mid
            else:
                left = mid + 1
        return left