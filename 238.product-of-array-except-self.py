#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        # finding prefix into ans
        for i in range(1,len(nums)):
            ans.append(nums[i-1]*ans[i-1])
        
        prev=1
        for i in range(len(nums)-2, -1, -1):
            if(i!=len(nums)):
                prev=prev*nums[i+1]
                ans[i]=prev*ans[i]
        return ans
        
        
        
# @lc code=end

