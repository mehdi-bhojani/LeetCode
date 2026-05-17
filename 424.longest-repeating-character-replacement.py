#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        occurances = [0]*26
        ans = 0
        max_occurance = 0

        for i in range(len(s)):
            occurances[s[i]-'A'] += +1
            max_occurance = max(max_occurance, occurances[s[i]-'A'])
            ans = 
        
# @lc code=end

