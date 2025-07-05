#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge case
        if len(nums)==0:
            return 0

        mySet = set()
        # inserting values in set
        for i in nums:
            mySet.add(i)
        
        longestSubSet = 0

        for i in mySet:
            # checking if the curr val is lead
            if(int(i-1) in mySet):
                continue
            else:
                curr = i
                localSub = 1
                while(int(curr + 1) in mySet):
                    localSub+=1
                    curr+=1
                longestSubSet = max(longestSubSet, localSub)
        
        return longestSubSet

        
# @lc code=end

