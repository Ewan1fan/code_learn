import collections
from typing import List

class Solution():
    def __init__(self) -> None:
        pass
    def subinteger(self,n:int) -> int:
        dp = [0]*(n+1) # 0,1,2,...,n
        dp[2] = 1#从2开始初始化，dp[2] = 1
        for i in range(3,n+1):
            for j in range(2,i):
                dp[i] = max(dp[i],max((i-j)*j,dp[j]*(i-j)))
            print(dp[i])
        return dp[-1]
    
s = Solution()
print(s.subinteger(11))

