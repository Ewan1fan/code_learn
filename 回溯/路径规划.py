from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets = sorted(tickets,key = lambda x:x[1])
        self.curpath = []
        # self.curpath.append("JFK")
        self.dic = {}
        for [key,val] in tickets:
            self.dic.setdefault(key,[]).append(val)
        print(self.dic)

        def backtracing(tickets,startkey):

            while startkey in self.dic and self.dic[startkey]:
                nextkey = self.dic[startkey][0]
                self.dic[startkey].pop(0)
                backtracing(tickets,nextkey)
                # self.dic[startkey].insert(0,nextkey)
            self.curpath.append(startkey)


        backtracing(tickets,'JFK')
        return self.curpath[::-1]
s = Solution()
print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
# tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
# tickets = sorted(tickets,key = lambda x:x[1])
# dic = {}
# for [key,val] in tickets:
#     dic.setdefault(key,[]).append(val)
# print(dic)