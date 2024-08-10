from typing import List
class treenode():
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: treenode) -> List[int]:
        res = []
        
        def dfs(node):
            if node is None:
                return
            

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
    def preorderTraversal1(self, root:treenode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res


t1 = treenode(5)
t2 = treenode(3)
t3 = treenode(2)
t4 = treenode(4)
t5 = treenode(1)
t6 = treenode(6)
t7 = treenode(7)
t1.left = t2
t1.right = t3

t2.left = t4
t2.right = t5

t3.left = t6
t3.right = t7

list = []
sol = Solution()
l = sol.preorderTraversal1(t1)
print(l)