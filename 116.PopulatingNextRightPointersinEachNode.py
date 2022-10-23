# Definition for a Node.
class Node:
    def __init__(self, val=0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

#实在想不出递归的方法，可以先试下用栈来做吧
#如果要有这种方式遍历，你可以想一下应该是BFS而不是DFS
class Solution:
    def connect(self, root):
        if root==None:
            return
        queue=[(root,0)]
        while queue:
            tmp=queue[0]
            # print(tmp[0].val,tmp[1])
            del queue[0]
            if queue:
                if queue[0][1]==tmp[1]:
                    tmp[0].next=queue[0][0]
                    # print(tmp[0].val,queue[0][0].val)
            if tmp[0].left:
                queue.append((tmp[0].left,tmp[1]+1))
            if tmp[0].right:
                queue.append((tmp[0].right,tmp[1]+1))
        return root

#想一想这道题的递归形式

def main():
    s=Solution()
    t=Node(1)
    t.left=Node(2)
    t.right=Node(3)
    t.left.left=Node(4)
    t.left.right=Node(5)
    t.right.left=Node(6)
    t.right.right=Node(7)
    t.left.left.left=Node(8)
    t.left.left.right=Node(9)
    t.left.right.left=Node(10)
    t.left.right.right=Node(11)
    t.right.left.left=Node(12)
    t.right.left.right=Node(13)
    t.right.right.left=Node(14)
    t.right.right.right=Node(15)
    s.connect(t)
    # print(t.left.next.val)
    # print(t.left.left.next.next.val)

main()