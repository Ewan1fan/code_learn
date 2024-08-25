from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.subpath = []
        self.path = []

        def backtracing(n,startindex,k):
            if len(self.subpath) == k:
                self.path.append(self.subpath[:])
                return
            for i in range(startindex,n+1):
                self.subpath.append(i)
                backtracing(n,i+1,k)
                self.subpath.pop()
        backtracing(n,1,k)
        return self.path
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.subpath = []
        self.path = []

        def backtracing(n,startindex,k):
            if len(self.subpath) == k:

                self.path.append(self.subpath.copy())#深浅复制
                return
            for i in range(startindex,n - (k - len(self.path)) + 2):
                self.subpath.append(i)
                backtracing(n,i+1,k)#k是一个恒定的量，尤其还涉及到判断，甚至在回溯中可能叠加减小为零，这个剪枝只能用它来推导，不能直接动它
                self.subpath.pop()
        backtracing(n,1,k)
        return self.path

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.curpath = []
        self.path = []
        # startindex = 1
        def bactracing(n,k,startindex):
            if len(self.curpath) == k:
                if sum(self.curpath) == n:
                    self.path.append(self.curpath.copy())
                return 
            for i in range(startindex,10 - (k-len(self.curpath))+1): #1,2,....,9 -> idx= 1,2,3,....,10
                if i > n - sum(self.curpath):
                    break
                self.curpath.append(i)
                bactracing(n,k,i+1)

                self.curpath.pop()
        bactracing(n,k,1)
        return self.path
    
s = Solution()
print(s.combinationSum3(9,45))
# a=[]
# b=[1,2]
# a.append(b)
# print(a)
# b.pop()
# print(a)
# b=[1,2]
# print(a)
# print(sum(a))
n=10
for i in range(n,-1,-1):
    print(i)

a = 'aba'
# print(a==a[::-1])
print(reversed(a))
print(a==reversed(a))
# print(a==a.reverse())
# 在 Python 中，字符串 (str) 是不可变的类型，这意味着一旦创建，就不能直接修改。因此，字符串对象本身没有像列表 (list) 那样的 reverse() 方法。
# list 的 reverse() 方法是就地(reverse in place)修改列表，而字符串没有类似的就地修改方法