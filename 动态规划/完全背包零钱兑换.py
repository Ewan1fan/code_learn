from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        # 遍历物品
        for i in range(len(coins)):
            # 遍历背包
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
            print(dp)
        return dp[amount]
    def change1(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        # 遍历物品
        for j in range(amount + 1):
            # 遍历背包
            for i in range(len(coins)):
                if j >= coins[i]:
                    dp[j] += dp[j - coins[i]]
            print(dp)
        return dp[amount]
    
s = Solution()
print(s.change1(amount = 5, coins = [1, 2, 5]))