# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dh = ListNode()

        while head:
            temp = ListNode(head.val)
            head = head.next
            temp.next = dh.next
            dh.next = temp


        return dh.next