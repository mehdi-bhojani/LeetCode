#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]
        reverese = [1]
        for i in range(1,len(nums)):
            forward.append(forward[i-1]*nums[i-1])
        
        prev=1
        for i in range(len(nums)-2,-1,-1):
            prev=prev*nums[i+1]
            forward[i]=forward[i]*prev
                
        print(forward)
        return forward

        
# @lc code=end