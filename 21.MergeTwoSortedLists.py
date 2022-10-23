class Solution:
    def mergeTwoLists(self, l1, l2):
        l=ListNode(0)
        p=l
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                tmp=ListNode(l1.val)
                p.next=tmp
                p=p.next
                l1=l1.next
            else:
                tmp=ListNode(l2.val)
                p.next=tmp
                p=p.next
                l2=l2.next
        if l1==None:
            while l2!=None:
                tmp=ListNode(l2.val)
                p.next=tmp
                p=p.next
                l2=l2.next
        if l2==None:
            while l1!=None:
                tmp=ListNode(l1.val)
                p.next=tmp
                p=p.next
                l1=l1.next
        l.next.printNode()
        return l.next