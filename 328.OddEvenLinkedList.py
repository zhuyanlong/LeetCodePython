# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head):
        h = ListNode(0)
        h.next = head
        tmp = h
        ht = tmp
        while h.next != None:
            h = h.next
            tmp.next = h.next
            tmp = tmp.next
            if tmp != None:
                h.next = tmp.next
                tmp.next = None
                
        h.next = ht.next
        return head
    
def main():
    head = ListNode(2)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(6)
    head.next.next.next.next.next = ListNode(4)
    # head.next.next.next.next.next.next = ListNode(7)
    sol = Solution()
    sol.oddEvenList(head)
    print(sol)

main()