class mylinklist:
    def __init__(self,val=-1,nextnode=None):
        self.val = val
        self.next = nextnode

class LRUCache:
    def __init__(self, capacity: int):
        self.datadic = {}
        self.LRUstack = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.datadic:
            self.LRUstack.remove(key)
            self.LRUstack.append(key)
            return self.datadic[key]
        else:

            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.datadic:
            self.LRUstack.remove(key)
            self.LRUstack.append(key)
            self.datadic[key] = value
        else:
            if len(self.datadic) < self.capacity:
                self.LRUstack.append(key)
                self.datadic[key] = value
            else:
                d = self.LRUstack.pop(0)
                del self.datadic[d]
                self.LRUstack.append(key)
                self.datadic[key] = value

class dLinkList:
    def __init__(self,val:int = None ,key:int = None,pre = None,next = None):
        self.val = val
        self.key = key
        self.pre = pre
        self.next = next
class LRUCache1:
     
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.dummyhead = dLinkList()
        self.dummytail = dLinkList()
        self.dummyhead.next = self.dummytail
        self.dummytail.pre = self.dummyhead

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        curnode = self.dic[key]
        
        curnode.pre.next = curnode.next
        curnode.next.pre = curnode.pre

        curnode.pre = self.dummyhead
        curnode.next = self.dummyhead.next
        self.dummyhead.next.pre = curnode
        self.dummyhead.next = curnode
        return curnode.val
            

    def put(self, key: int, value: int) -> None:

        if key in self.dic:
            curnode = self.dic[key]
            curnode.val = value

            curnode.pre.next = curnode.next
            curnode.next.pre = curnode.pre

            curnode.pre = self.dummyhead
            curnode.next = self.dummyhead.next
            self.dummyhead.next.pre = curnode
            self.dummyhead.next = curnode
 
        else:
            if len(self.dic) < self.capacity:
                curnode = dLinkList(value,key)

                curnode.pre = self.dummyhead
                curnode.next = self.dummyhead.next
                self.dummyhead.next.pre = curnode
                self.dummyhead.next = curnode
                self.dic[key] = curnode
            else:
                curnode = dLinkList(value,key)

                curnode.pre = self.dummyhead
                curnode.next = self.dummyhead.next
                self.dummyhead.next.pre = curnode
                self.dummyhead.next = curnode
                del self.dic[self.dummytail.pre.key]
                self.dummytail.pre = self.dummytail.pre.pre
                self.dummytail.pre.next = self.dummytail
                self.dic[key] = curnode

            




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)