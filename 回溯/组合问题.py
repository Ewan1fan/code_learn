from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []

        def traceback(i: int, n, k):  # 左闭右开
            if len(temp) == k:
                print(temp)
                temp.clear()
                return
            if i == n + 1:
                return
            temp.append(i)
            print()
            traceback(i + 1, n, k)

        traceback(1, n, k)
        return res
# s = Solution()
# print(s.combine(4,2))
dic = {}
dic.setdefault('a', []).append(1)
print(dic)
print([[key,val] for key,val in enumerate([1,1,2])])