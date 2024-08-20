from typing import List

class solution():

    def package(self,value:List[int],item_weight:List[int],package_weight:int)->int:
        #初始化DP数组
        maxvalue = [[0]*(package_weight+1) for _ in range(len(value))]
        for i in range(package_weight+1):
            if i >= item_weight[0]:
                maxvalue[0][i] = value[0]

        # 推导式
        for i in range(1,len(item_weight)):
            for j in range(package_weight+1):
                if item_weight[i] > j:
                    maxvalue[i][j] = maxvalue[i-1][j]
                else:
                    # print(value[i]+maxvalue[i-1][j-item_weight[i]])
                    # print(maxvalue[i-1][j])
                    maxvalue[i][j] = max(maxvalue[i-1][j],value[i]+maxvalue[i-1][j-item_weight[i]])
        return maxvalue
    
s = solution()
item_weight = [1,3,4]
value = [15,20,30]
package_weight = 15
print(s.package(value,item_weight,package_weight))