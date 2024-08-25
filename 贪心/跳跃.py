from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        maxindex = nums[0]
        cur = 0
        while cur <= maxindex:
            if maxindex >=len(nums)-1:
                return True
            cur += 1
            maxindex = max(maxindex,cur+nums[cur])
        return False
    
s = Solution()
s.canJump([3,2,1,0,4])