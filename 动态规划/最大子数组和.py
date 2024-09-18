from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-float('inf')] * (len(nums)+1)
        print(dp)
        result = -float('inf')
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i-1],nums[i-1])
            print(nums[i-1])
            print(dp[i])
            result = max(result,dp[i])
        return result

s = Solution()
print(s.maxSubArray([1]))