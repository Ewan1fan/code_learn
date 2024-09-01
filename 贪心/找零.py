from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = [0,0]
        b1 = True
        b2 = True
        for i in range(len(bills)):
            if bills[i] == 5:
                dic[0]+=1
            elif bills[i] == 10:
                if dic[0]:
                    dic[0] -= 1
                    dic[1] +=1
                else:
                    return False
            elif bills[i] == 20:
                    if dic[1]:
                        dic[1] -= 1
                        if dic[0]:
                            dic[0] -=1
                        else:
                            b1 = False
                    else:
                        if dic[0] >= 3:
                            dic[0] -= 3
                        else:
                            b2 = False
                    if not b1 and not b2:

                        return False
        return True

s = Solution()
print(s.lemonadeChange([5,5,10,10,20]))