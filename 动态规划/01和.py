from typing import List


class Solution:
    def findprice(self,s):
        a = [0,0]
        for i in range(len(s)):
            if s[i] == '0':
                a[0] += 1
            else:
                a[1] += 1
        return a
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[]]*(n+1) for _ in range(m+1)]
        for s in strs:
            sPrice = self.findprice(s)
            for i in range(m,-1,-1):
                for j in range(n,-1,-1):
                    if i >= sPrice[0] and j >= sPrice[1]:
                        temp = dp[i-sPrice[0]][j-sPrice[1]].copy()
                        temp.append(s)
                        if len(dp[i][j]) < len(temp):
                            dp[i][j] = temp
                        elif len(dp[i][j]) == len(temp):
                            dp[i][j] = max(temp,dp[i][j],key = lambda x:sum(self.findprice(x)))
                            # dp[i][j] = max(temp,dp[i][j],key = lambda x:len(x))
        return dp[-1][-1]
    
s = Solution()
print(s.findMaxForm(["10","0001","111001","1","0"],5,3))