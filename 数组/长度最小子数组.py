from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        fast = 0
        res =float('inf')
        s = 0
        for i in range(len(nums)):
            if s < target:
                s += nums[fast]
                fast += 1
            else:
                res = min(res,fast - slow)
                s -= nums[slow]
                slow += 1
        return res if res != float('inf') else 0
    
s = Solution()
s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])