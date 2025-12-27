# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp1=head
        if temp1.next is None:
            return None
        while temp1 is not None:
            count+=1
            temp1=temp1.next
        temp2=head
        prev=temp2
        i=0
        while i<count//2:
            prev=temp2
            temp2=temp2.next
            i+=1
        prev.next=temp2.next
        return head
            

