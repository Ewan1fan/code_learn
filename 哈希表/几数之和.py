from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [] if  sum(nums) else [nums]
        s = set()
        res = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                # s.add(nums[i]+nums[j])
                
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        s.add([nums[i],nums[j],nums[k]])
        return 
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(1 in {-1})