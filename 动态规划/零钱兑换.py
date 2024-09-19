from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0,0] for i in range(amount + 1)]
        for c in coins:
            for i in range(c,amount+1):
                if not dp[i]:
                    dp[i][0] = dp[i-c][0] + 1
                    dp[i][1] = dp[i-c][1]+ c
                else:
                    if dp[i-c][0]+1 < dp[i][0]:
                        dp[i][0] = dp[i-c][0] + 1
                        dp[i][1] = dp[i-c][1] + c
                    else:
                        dp[i][0] = dp[i][0]
                        dp[i][1] = dp[i][1]
        print(dp)
        if dp[amount][1] == amount:
            return dp[amount][0]
        else:
            return -1
        
s = Solution()
print(s.coinChange(coins = [1, 2, 5], amount = 11))