#Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        s=head
        f=head
        if(head is None):
            return head
        else:
            while(f is not None and f.next is not None):
                s=s.next
                f=f.next.next
            return s
