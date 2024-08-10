from typing import List

class treenode():
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal1(self, root:treenode) -> List[int]:
        res = []
        stack = [root]
        if root == None:
            return res
        # stack.append(root)
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            res.append(cur.val)
        return res
    def preorderTraversal2(self, root:treenode) -> List[int]:
        res = []
        stack = [root]
        if root == None:
            return res
        # stack.append(root)
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.left)
            if cur.left:
                stack.append(cur.right)
            res.append(cur.val)
        return res[::-1]
    def preorderTraversal3(self, root:treenode) -> List[int]:
        res = []
        stack = []
        ptr = root
        if root == None:
            return res
        # stack.append(root)
        while stack:
            while ptr.left:
                stack.append(ptr.left)
                ptr = ptr.left
            res.append(stack.pop())
            ptr = stack.pop()
            res.append(ptr)
            ptr = ptr.right

            
        return res


t1 = treenode(5)
t2 = treenode(3)
t3 = treenode(2)
t4 = treenode(4)
t5 = treenode(1)
t6 = treenode(6)
t7 = treenode(7)

#    5
#   3 2
# 4 1 6 7

t1.left = t2
t1.right = t3

t2.left = t4
t2.right = t5

t3.left = t6
t3.right = t7

list = []
sol = Solution()
l = sol.preorderTraversal3(t1)
print(l)