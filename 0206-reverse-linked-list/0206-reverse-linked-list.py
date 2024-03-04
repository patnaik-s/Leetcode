# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev


#recursive
"""
if not head:
    return none
newhead=head
if head.node:
   newhead =  self.reverse(head.next)
   head.ext.next=head
head.nex=tnone 
return newhead
"""
#->1->2