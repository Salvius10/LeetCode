# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        left=head
        right=head.next
        while left and left.next:
            right=left.next
            left.val,right.val=right.val,left.val
            left=right.next
        return head

        