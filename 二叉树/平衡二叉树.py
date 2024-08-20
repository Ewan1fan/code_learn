
from typing import List
import queue
import collections
class treenode():
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        def depth(node):
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            if l == -1 or r == -1:
                return -1
            if abs(l-r)>1:
                return -1
            return max(l,r)+1
        return True if depth(root) != -1 else False
    def findBottomLeftValue(self, root) -> int:
        maxheight = 1
        res = root.val
        def dfs(node,height,maxheight,res):
            if node == None:
                return res,maxheight
            if not node.left and not node.right:
                return res,maxheight
            res,maxheight = dfs(node.left,height+1,maxheight,res)
            if node.left and not node.left.left and not node.left.right:
                if maxheight < height+1 :
                    maxheight = height+1
                    res = node.left.val
            if not node.left and node.right and not node.right.left and not node.right.right:
                if maxheight < height+1 :
                    maxheight = height+1
                    res = node.right.val
            res,maxheight = dfs(node.right,height+1,maxheight,res)

            return res,maxheight
        return dfs(root,1,maxheight,res)[0]
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

# list = []
# sol = Solution()
# l = sol.findBottomLeftValue(t1)
# print(l)
print(max([1,2,3,4]))
