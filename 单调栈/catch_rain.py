from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        # if len(height)<3:
        #     return res

        stack = [0]
        for i in range(1,len(height)):
            while stack and height[i] > height[stack[-1]]:
                if len(stack) > 1:
                    h = min(height[i],height[stack[-2]])-height[stack[-1]]
                    w = i - stack[-2] -1
                    res += h * w 
                stack.pop()
            stack.append(i)
        return res
    def MaxArea(self, height: List[int]) -> int:
        stack = [-1]
        # max_area = - float('inf')
        max_area = 0
        height.append(0)
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                cur = stack.pop()
                if stack:
                    h = height[cur]
                    w = i - stack[-1] -1
                    if max_area < h*w:
                        max_area = h*w
            stack.append(i)
        return max_area

# temperatures2 = [0,1,0,2,1,0,1,3,2,1,2,1]
temperatures2 = [4,2]
# temperatures2 = [2,1,2,1,1,0]

s = Solution()
print(s.MaxArea(temperatures2))