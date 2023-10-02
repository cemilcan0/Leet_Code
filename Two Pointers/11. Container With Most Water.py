class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        val = 0
        left = 0
        right = len(height)-1

        while left<right:
            if(height[left]<height[right]):
                temp = height[left]*(right-left)
                if(temp>val):
                    val = temp
                left+=1      
            else:
                temp = height[right]*(right-left)
                if(temp>val):
                    val = temp
                right-=1
        return val
                