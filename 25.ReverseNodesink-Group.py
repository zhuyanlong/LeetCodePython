# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverse(self, start, end):
        newhead=ListNode(0); newhead.next=start
        while newhead.next!=end:
            tmp=start.next
            start.next=tmp.next
            tmp.next=newhead.next
            newhead.next=tmp
        return [end, start]
    def reverseKGroup(self, head, k):
        if head==None: return None
        nhead=ListNode(0); nhead.next=head; start=nhead
        while start.next:
            end=start
            for i in range(k-1):
                end=end.next
                if end.next==None: return nhead.next
            res=self.reverse(start.next, end.next)
            start.next=res[0]
            start=res[1]
        return nhead.next


def main():
    l=ListNode(1)
    l.next=ListNode(2)
    l.next.next=ListNode(3)
    l.next.next.next=ListNode(4)
    l.next.next.next.next=ListNode(5)
    t=l.next
    s=Solution()
    k=2
    l=s.reverseKGroup(l,k)
    # s.printNode(t)

main()