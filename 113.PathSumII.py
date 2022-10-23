# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, sum):
        if root ==None:
            return []
        stack=[(root,0)]
        res=[]
        val=[]
        while stack:
            tmp=stack.pop()
            while len(val)!=tmp[1]:
                val.pop()
            val.append(tmp[0].val)
            if tmp[0].left:
                stack.append((tmp[0].left,tmp[1]+1))
            if tmp[0].right:
                stack.append((tmp[0].right,tmp[1]+1))
            if tmp[0].left==None and tmp[0].right==None:
                s=0
                for item in val:
                    s+=item
                if s==sum:
                    res.append(val.copy())
        # print(res)
        return res

def main():
    t=TreeNode(5)
    t.left=TreeNode(4)
    t.right=TreeNode(8)
    t.left.left=TreeNode(11)
    t.left.left.left=TreeNode(7)
    t.left.left.right=TreeNode(2)
    t.right.left=TreeNode(13)
    t.right.right=TreeNode(4)
    t.right.right.left=TreeNode(5)
    t.right.right.right=TreeNode(1)
    s=Solution()
    su=22
    s.pathSum(t,su)

main()