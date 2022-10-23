# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#这种问题被成为LCA问题，我还没有想出很好的解决这种问题的方式
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p==root or q==root:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right

# 栈法遍历得到两条路径，比价获得公共祖先节点
class Solution:
    def lowestCommonAncestor(self, root, p, q) :
        pp=[]
        pq=[]
        self.findPath(pp,[(root,0)],p)
        self.findPath(pq,[(root,0)],q)
        res=root
        for i in range(len(pp)):
            if pp[i] in pq:
                res=pp[i]
        return res
        
    def findPath(self,path,stack,target):
        while stack:
            tmp=stack.pop()
            while len(path)!=tmp[1]:
                path.pop()
            path.append(tmp[0])
            if tmp[0]==target:
                return
            if tmp[0].left:
                stack.append((tmp[0].left,tmp[1]+1))
            if tmp[0].right:
                stack.append((tmp[0].right,tmp[1]+1))