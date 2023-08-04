from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        array = [1] * n
        left = right = 1
        for i in range(n):
            array[i] *= left
            left *= nums[i]
        
        for i in range(n-1, -1, -1):
            array[i] *= right
            right *= nums[i]
        
        return array