#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=prices[0]
        profit=0

        for i in range(len(prices)):
            low = min(low, prices[i])
            profit = 0
            if(prices[i]>low):
                profit = max(profit, prices[i]-low)
                print(profit)
            
            return profit

        
# @lc code=end

