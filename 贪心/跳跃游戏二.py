from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxindex = 0
        count = 0
        i = 0
        while i <= maxindex:

            for i in range(i,maxindex+1):
                maxindex = max(maxindex,i+nums[i])
                if maxindex >=len(nums)-1:
                    return count+1
            count+=1
        return 0
    
s = Solution()
print(s.jump([1,1,1,1,1]))