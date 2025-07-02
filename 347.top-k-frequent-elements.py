#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict={}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]]+=1
            else:
                my_dict[nums[i]]=1
        
        topkitems = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)[:k]
        ans = list(map(operator.itemgetter(0),topkitems))
        return ans


        
# @lc code=end

