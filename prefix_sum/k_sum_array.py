from typing import List


class Solution:
    def __init__(self):
        pass

    def k_sum_subarray(self, nums: List[int], k: int) -> int:
        count = 0
        sum_map = {0: 1}
        curr_prefix_sum = 0
        for num in nums:
            curr_prefix_sum += num
            if curr_prefix_sum - k in sum_map:
                count += sum_map[curr_prefix_sum - k]
            freq = sum_map.get(curr_prefix_sum, 0)
            sum_map[curr_prefix_sum] = freq + 1
        return count
