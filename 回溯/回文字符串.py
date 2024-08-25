from typing import List
class Solution:
    def ifreverse(self,s:List[str])->bool:
        for i in range(len(s)):
            if s[i] != s[i][::-1]:
                return False
        return True
    def partition(self, s: str) -> List[List[str]]:
        self.curpath = []
        self.path = []
        def backtracing(s,startindex):
            if startindex == len(s):
                self.path.append(self.curpath.copy())
                return 
            for i in range(startindex,len(s)):
                if self.ifreverse(s[startindex:i+1]):
                    self.curpath.append(s[startindex:i+1])
                    backtracing(s,i+1)
                    self.curpath.pop()
        backtracing(s,0)
        return self.path

a = 'aab'

s = Solution()
print(s.partition(a))
print(int('233')-1)