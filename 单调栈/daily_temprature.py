from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        cur = 0
        ptr = 0
        res=[]
        for i in range(len(temperatures)-1):
            # while(temperatures[ptr] <= temperatures[cur] and ptr < len(temperatures)):
            for j in range(cur,len(temperatures)-1):
                if(temperatures[ptr] <= temperatures[cur]):
                    ptr+=1
                else:
                    break

            if ptr == len(temperatures)-1:
                if(temperatures[ptr] <= temperatures[cur]):
                    res.append(0)
                else:
                    res.append(ptr-cur)

            else:
                res.append(ptr-cur)
            # print(i)
            cur += 1
            ptr = cur
        res.append(0)
        return(res)
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
            stack = []
            stack.append(0)
            i = 1
            while stack:
                if i == len(temperatures):
                    for j in range(len(stack)):
                        temperatures[stack.pop()]=0
                    break
                for h in range(len(stack)):
                    if temperatures[stack[-1]] < temperatures[i]:
                        temperatures[stack.pop()] = i - stack[-1]
                    else:
                        break
                stack.append(i)
                print(stack)
                # print(temperatures)
                i += 1
            return(temperatures)
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
            stack = []
            stack.append(0)
            res = [0]*len(temperatures)
            i = 1
            while stack and i<len(temperatures):

                for h in range(len(stack)):
                    if temperatures[stack[-1]] < temperatures[i]:
                        res[stack.pop()] = i - stack[-1]
                    else:
                        break
                stack.append(i)
                print(stack)
                i += 1
            return(res)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res1 = [-1]*len(nums1)
        dic = {}
        for j in range(len(nums1)):
            dic[nums1[j]] = j
        stack = [0]
        for i in range(1,len(nums2)):
            while(stack and nums2[i] > nums2[stack[-1]] ):
                if nums2[stack[-1]] in dic:
                    res1[dic[nums2[stack[-1]]]] = nums2[i]
                stack.pop()
            stack.append(i)
        return res1
    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        res = [-1]*(2*len(nums))
        stack = [0]
        nums1 = nums+nums
        for i in range(1, len(nums1)):
            while stack and nums1[i]> nums1[stack[-1]]:
                res[stack[-1]] = nums1[i]
                stack.pop()
            stack.append(i)

        return res[:len(nums)]
temperatures1 = [2,4]
temperatures2 = [1,2,3,4]
#[1,2,-1]
#[2,1,2,1,1,0]

s = Solution()
print(s.nextGreaterElement(temperatures1,temperatures2))
