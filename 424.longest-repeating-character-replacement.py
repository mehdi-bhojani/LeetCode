#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 1
        myDictionary = {}
        result = 0
        length = len(s)
        ans=0
        max_occurance=0

        while(left<=length):
            if s[left-1] not in myDictionary:
                myDictionary[s[left-1]]=0
            myDictionary[s[left-1]] += 1
            max_occurance = max(max_occurance,myDictionary[s[left-1]])
            print(max_occurance)
            if (left - right + 1 - max_occurance) <= k:
                ans = left - right + 1
            else: 
                myDictionary[s[right-1]]=myDictionary[s[right-1]]-1
                right=right+1
            result= max(result,ans)
            left=left+1
        
        return result
        
# @lc code=end


