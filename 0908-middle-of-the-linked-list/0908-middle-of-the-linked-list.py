# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=head
        temp=head
        while temp and temp.next is not None:
            prev=prev.next
            temp=temp.next.next
        return prev

        