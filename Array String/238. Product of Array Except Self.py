from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        çarp = [1] * n
        left = right = 1
        for i in range(n):
            çarp[i] *= left
            left *= nums[i]
        
        for i in range(n-1, -1, -1):
            çarp[i] *= right
            right *= nums[i]
        
        return çarp