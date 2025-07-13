#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        total=0
        LMax=height[left]
        RMax=height[right]
        while(left<right):
            if(height[left]<height[right]):
                LMax= max(LMax, height[left])
                if((LMax - height[left])>0):
                    total+=(LMax - height[left])
                left+=1
            else:
                RMax= max(RMax, height[right])
                if((RMax - height[right])>0):
                    total+=(RMax - height[right])
                right-=1
        return total

        
# @lc code=end

