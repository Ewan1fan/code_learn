from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set()
        s2 = set()
        res = []
        for i in range(len(nums1)):
            s1.add(nums1[i])
        for j in range(len(nums2)):
            s2.add(nums2[j])
        for n in s1:
            if n in s2:
                res.append(n)
        return res
print([[key,val] for key,val in enumerate([1,1,2])])