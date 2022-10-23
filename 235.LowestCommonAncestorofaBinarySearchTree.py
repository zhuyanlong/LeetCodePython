# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#迭代法
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         maxval=0
#         minval=0
#         if p.val>q.val:
#             maxval=p.val
#             minval=q.val
#         else:
#             maxval=q.val
#             minval=p.val
#         tmp=root
#         while tmp!=None:
#             if maxval>=tmp.val and minval<=tmp.val:
#                 return tmp
#             else:
#                 if minval>=tmp.val:
#                     tmp=tmp.right
#                 elif maxval<=tmp.val:
#                     tmp=tmp.left
#         return None

#递归法
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
