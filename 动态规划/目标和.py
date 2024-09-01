from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums) - target) % 2 != 0 or sum(nums) < target:
            return 0
        s = (sum(nums) - target) // 2
        dp = [0]*(s+1)
        dp[0] = 1
        for num in nums:
            for i in range(s,-1,-1):
                if i >= num:
                    dp[i] = dp[i]+dp[i-num]
            print(dp)
        return dp[-1]
    
s = Solution()
print(s.findTargetSumWays(
[2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53],1000
))
