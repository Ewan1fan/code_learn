from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [0] * l
        m = prices[0]
        for i in range(l):
            m = min(m,prices[i])
            dp[i] = prices[i] - m
        return max(dp)
    
s = Solution()
s.maxProfit([7,1,5,3,6,4])