from typing import List

class Solution:
    def __init__(self):
        pass
    
    def product_array_without_self(self, nums: List[int]):
        res = [1]
        for i in range(1, len(nums)):
            res.append(res[i-1] * nums[i-1])
        
        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i+1]
            res[i] *= right_product
        
        return res