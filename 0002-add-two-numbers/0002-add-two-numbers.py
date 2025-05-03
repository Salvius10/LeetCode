# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        temp=dummy
        carry=0
        while l1 or l2:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            result=val1+val2+carry
            carry=result//10
            current=ListNode(result%10)
            temp.next=current
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            temp=temp.next
        if carry!=0:
            current=ListNode(carry)
            temp.next=current
            temp=temp.next
        return dummy.next

        
        