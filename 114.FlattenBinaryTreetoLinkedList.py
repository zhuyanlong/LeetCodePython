# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#思路很好想，首先找到最左子节点，然后插到父节点和右子节点之间，不断重复这个过程
class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left==None:
            return
        tmp=root.right
        root.right=root.left
        root.left=None
        while root.right:
            root=root.right
        root.right=tmp

    def printNode(self,root):
        if root==None:
            return 
        tmp=root
        while tmp!=None:
            print(tmp.val)
            tmp=tmp.right

def main():
    t=TreeNode(1)
    t.left=TreeNode(2)
    t.right=TreeNode(5)
    t.left.left=TreeNode(3)
    t.left.right=TreeNode(4)
    t.right.right=TreeNode(6)
    s=Solution()
    s.flatten(t)
    s.printNode(t)

main()