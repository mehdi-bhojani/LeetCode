#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        longest_len = 0
        left=0

        # base cae
        if len(s) == 0:
            return 0

        for right in range(len(s)):
            # checking from set and removing left 2 right
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            # adding in visited
            visited.add(s[right])
            longest_len=max(longest_len,right-left+1)
        
        return longest_len
            



# @lc code=end

