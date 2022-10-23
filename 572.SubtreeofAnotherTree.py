# Definition for a binary tree node.
# 实际上遍历是可以的，那天没有想错，唯一的一点就是，遍历出的字符串要倒着判断，这点你当时没有想到
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root, subRoot):
        resinA=[]
        self.inorder(resinA,root)
        resinB=[]
        self.inorder(resinB,subRoot)
        if "".join(resinB) not in "".join(resinA):
            print(resinB,resinA)
            return False
        print(resinB,resinA)
        respreA=[]
        self.postorder(respreA,root)
        respreB=[]
        self.postorder(respreB,subRoot)
        # if "".join(respreB) not in "".join(respreA):
        #     print(respreB,respreA)
        #     return False
        for i in range(len(respreB)):
            if respreB[i]!=respreA[i]:
                return False
        print(respreB,respreA)
        return True

    def inorder(self,res,root):
        if root==None:
            return
        self.inorder(res,root.left)
        res.append(str(root.val))
        self.inorder(res,root.right)

    def preorder(self,res,root):
        if root==None:
            return
        res.append(str(root.val))
        self.preorder(res,root.left)
        self.preorder(res,root.right)

    def postorder(self,res,root):
        if root==None:
            return
        self.postorder(res,root.left)
        self.postorder(res,root.right)
        res.append(str(root.val))

def main():
    root=TreeNode(3)
    root.left=TreeNode(4)
    root.right=TreeNode(5)
    root.left.left=TreeNode(1)
    root.left.right=TreeNode(2)
    # root.left.right.left=TreeNode(0)
    subRoot=TreeNode(4)
    subRoot.left=TreeNode(1)
    subRoot.right=TreeNode(2)
    # root=TreeNode(1)
    # root.left=TreeNode(2)
    # root.right=TreeNode(3)
    # subRoot=TreeNode(1)
    # subRoot.left=TreeNode(2)
    sol=Solution()
    res=sol.isSubtree(root,subRoot)
    print(res)

main()