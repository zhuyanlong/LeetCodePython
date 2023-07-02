class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None:
            return
        h=ListNode()
        h.next=head
        slow=h.next
        fast=h.next
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        if slow==fast:
            return h.next
        fast=slow.next
        slow.next=None
        # 倒排链表
        last=fast
        while last.next!=None:
            last=last.next
        tmp=fast.next
        while fast!=last:
            fast.next=last.next
            last.next=fast
            fast=tmp
            tmp=tmp.next
        first=h.next
        while last!=None:
            tmp=last
            last=last.next
            tmp.next=first.next
            first.next=tmp
            first=tmp.next
        return  h.next    