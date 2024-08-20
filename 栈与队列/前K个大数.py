from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        h = []
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i],0)+1
        for key,val in dic.items():
            heapq.heappush(h,(val,key))#元组可以，List行吗
            while len(h) > k:
                heapq.heappop(h)
            
        return [x[1] for x in h][::-1]