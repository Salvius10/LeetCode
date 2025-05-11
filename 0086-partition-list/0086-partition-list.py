# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp=head
        dummy1=ListNode(0)
        before=dummy1
        dummy2=ListNode(0)
        after=dummy2
        while temp:
            if temp.val<x:
                before.next=temp
                before=before.next
                temp=temp.next
            else:
                after.next=temp
                after=after.next
                temp=temp.next
        after.next=None
        before.next=dummy2.next
        return dummy1.next
        
            
        
        