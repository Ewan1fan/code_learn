from typing import List

class Solution:
    class MyPriorityQueue:
        def __init__(self) -> None:
            import collections
            self.queue = collections.deque()
        def pop(self, val:int) -> List[int]:
            if self.queue and self.front() == val:
                self.queue.popleft()
        def push(self,val:int) -> List[int]:
            if not self.queue:
                self.queue.append(val)
            else:
                if val > self.back():
                    while self.queue and val > self.back():
                        self.queue.pop()
                self.queue.append(val)
            return self.queue
        def front(self) -> int:
            return self.queue[0]
        def back(self) -> int:
            return self.queue[-1]
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        if len(nums)==1:
            return [nums[0]]
        h = self.MyPriorityQueue()
        for i in range(k):
            h.push(nums[i])
        res.append(h.front())
        for i in range(len(nums)-k):
            h.pop(nums[i])
            h.push(nums[i+k])
            res.append(h.front())
        return res

sol = Solution()
nums = [1,3,1,2,0,5]
k = 3
l = sol.maxSlidingWindow(nums,k)
print(l)