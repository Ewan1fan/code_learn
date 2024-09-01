from copy import deepcopy
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                for j in range(i,n):
                    dp[0][j] = 0
                break
        for h in range(m):
            if obstacleGrid[h][0] == 0:
                dp[h][0] = 1
            else:
                for k in range(h,m):
                    dp[k][0] = 0
                break
        for x in range(m):
            for y in range(n):
                if obstacleGrid[x][y] == 1:
                    dp[x][y] = 0
                dp[x][y] = dp[x-1][y] + dp[x][y-1]
        return dp[m-1][n-1]

s = Solution()
s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])