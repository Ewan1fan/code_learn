from typing import List
import queue
import collections
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
    def midorderTraversal(self, root:treenode) -> List[int]:
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
    def afterorderTraversal(self, root:treenode) -> List[int]:
        res = []
        stack = []
        ptr = root
        if root == None:
            return res
        # stack.append(root)
        while ptr or stack:
            if ptr:
                stack.append(ptr)
                ptr = ptr.left
                ##顺着往下等到第一个空指针
            else:
                res.append(stack[-1].val)
                #左侧指空后先加中再弹出指向右，右侧再作为子树的中先加进去**先不处理**
                #右侧指空本子树遍历完成，本子树的中在指向右的时候已经处理了（左中右），返回的是上个子树
                ptr = stack.pop().right
                #弹出左指到右
            # print(res)

    def traversal(self,root:treenode)-> List[int]:
        res = []
        if not root:
            return res
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
    def traversal1(self,root:treenode)-> List[int]:
        res = []
        stack = []
        # def print_val(ls):
        #     if ls:
        #         for i in range(len(ls)):
        #             if ls[i]:
        #                 print(ls[i].val)
        #             else:
        #                 print('None')
        #     else:
        #         print('[]')
        #     print('_______________________________')
        if root:
            stack.append(root)
        while stack:
            current = stack[-1]
            if current:
                stack.pop()#弹出，然后按照中左右或者其他遍历的顺序再倒着加进去
                stack.append(current)
                stack.append(None)#中
                if current.right: stack.append(current.right)#右
                if current.left: stack.append(current.left)#左

                
            else:
                stack.pop()
                res.append(stack.pop().val)
            # print_val(stack)
        return res
    def LevelOrderTraversal(self,root:treenode)-> List[int]:
        resolution = []
        if not root:
            return resolution
        que = queue.Queue()
        que.put(root)
        length = 1
        while(length):
            cur = que.get()            
            resolution.append(cur.val)
            length -= 1
            if cur.left: 
                que.put(cur.left)
                length+=1
            if cur.right: 
                que.put(cur.right)
                length+=1
        return resolution
    def LevelOrderTraversal2(self,root:treenode)-> List[int]:
        res = []
        if not root:
            return res
        que = collections.deque()
        que.appendleft(root)
        length = 1
        while(length):
            cur = que.pop()            
            res.append(cur.val)
            length -= 1
            if cur.left: 
                que.appendleft(cur.left)
                length+=1
            if cur.right: 
                que.appendleft(cur.right)
                length+=1
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

# t2.left = t4
t2.right = t5

t3.left = t6
t3.right = t7

list = []
sol = Solution()
l = sol.LevelOrderTraversal2(t1)
print(l)