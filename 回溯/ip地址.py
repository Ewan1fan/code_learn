from typing import List
class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.curpath = []
        self.path = []
        def ifvalid(s):
            if len(s) > 3:
                return False
            if len(s) > 1 and s[0] == '0':
                return False
            return 0<=int(s)<=255
        def backtracing(s):
            if len(self.curpath) < 3 and s=='':
                return
            if len(self.curpath) == 3:
                print(s)
                if ifvalid(s):
                    self.curpath.append(s)
                    self.path.append('.'.join(self.curpath.copy()))
                    self.curpath.pop()
                return
            for i in range(len(s)):
                if ifvalid(s[:i+1]):
                    self.curpath.append(s[:i+1])
                    backtracing(s[i+1:])
                    self.curpath.pop()
                else:
                    continue


        backtracing(s)
        return self.path

s = Solution()
print(s.restoreIpAddresses("25525511135"))