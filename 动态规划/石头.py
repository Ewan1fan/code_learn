from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones) // 2
        print(s)
        dp = [0] * (s+1)
        for n in stones:
            for j in range(s,0,-1):
                if j >= n:
                    dp[j] = max(dp[j],dp[j-n]+n)
        return sum(stones) - 2*dp[-1]

s = Solution()
print(s.lastStoneWeightII([2,7,4,1,8,1]))