from typing import List,Optional
import numpy as np
class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.right = right
        self.left = left
def bulidTree(cur:Optional[TreeNode],val_list:list[int])->Optional[TreeNode]:
    TreeNode_list = [TreeNode(x) for x in val_list] 
    for i in range(len(TreeNode_list)):
        cur = TreeNode_list[i]
        if 2*i+1 < len(val_list):
            cur.left = TreeNode_list[2*i+1]
        if 2*i+2 < len(val_list):
            cur.right = TreeNode_list[2*i+2]
    return TreeNode_list
def printTree(TreeNode_list:list[Optional[TreeNode]]):
    for i in range(len(TreeNode_list)):
        print(TreeNode_list[i].val)
class Solution():
    def __init__(self) -> None:
        pass
    def deleteNode(self, root:Optional[TreeNode],val:int)->Optional[TreeNode]:
        if not root:
            return root
        if root.val == val:
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
        if root.val < val:
            root.right = self.deleteNode(root.right,val)
        if root.val > val:
            root.left = self.deleteNode(root.left,val)
        return root


root = [5,3,6,2,4,None,7]#共计2^N-1个节点，N为层数
root_node = TreeNode(5)
node = bulidTree(root_node,root)[0]
printTree(bulidTree(root_node,root))
s1 = Solution()
s1.deleteNode(node,3)
