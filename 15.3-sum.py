#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
# Using 2 pointer Approach
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedList = sorted(nums)
        print(sortedList)

        ans = set()
        for i in range(len(sortedList)):
            # handle 2 dublc vals
            if(i>0 and sortedList[i]==sortedList[i-1]):
                continue

            left=i+1
            right=len(sortedList)-1
            print(left,right)
            while(left<right and sortedList[right]>=0):
                sum = sortedList[i] + sortedList[left] + sortedList[right]
                if(sum==0):
                    ans.add((sortedList[i], sortedList[left], sortedList[right]))
                    left+=1
                    right-=1
                elif(sum>0):
                    right-=1
                else:
                    left+=1
        return [list(i) for i in ans]
    

                



# @lc code=end

