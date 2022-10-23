# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def addNode(self,val):
        l=ListNode(val)
        tmp=self
        while tmp.next!=None:
            tmp=tmp.next
        tmp.next=l

    def printNode(self):
        tmp=self
        res=[]
        while tmp.next!=None:
            res.append(tmp.val)
            tmp=tmp.next
        res.append(tmp.val)
        print(res)

# class Solution:
#     def reverseList(self, head):
#         if head == None or head.next == None:
#             return head
#         c=head.next
#         p=c.next
#         head.next=None
#         while c.next!=None:
#             c.next=head
#             head=c
#             c=p
#             p=p.next
#         c.next=head
#         return c

class Solution:
    def reverseList(self, head):
        if head==None:
            return
        hnode=ListNode(0)
        hnode.next=head
        j=head
        while j.next!=None:
            j=j.next
        hnode.next=j
        while head!=j:
            k=head
            head=k.next
            k.next=j.next
            j.next=k
        return hnode.next

def main():
    l=ListNode(1)
    l.addNode(2)
    l.addNode(3)
    l.addNode(4)
    l.addNode(5)
    l.addNode(6)

    l.printNode()
    s=Solution
    s.reverseList(s,l).printNode()

main()