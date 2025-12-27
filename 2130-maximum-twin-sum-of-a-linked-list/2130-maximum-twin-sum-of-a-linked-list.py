# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n=0
        temp=head
        while temp is not None:
            n+=1
            temp=temp.next
        count=0
        mid=n//2
        curr=head
        while count<mid:
            count+=1
            curr=curr.next
        prev=None
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        left=head
        right=prev
        a=0
        while right is not None:
            a=max(a,left.val+right.val)
            left=left.next
            right=right.next
        return a
