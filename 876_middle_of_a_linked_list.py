# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner1 = head
        runner2 = head

        counter = 0

        while runner1:
            runner1 = runner1.next
            counter +=1

        counter = counter//2
        print(counter)

        for i in range(counter):
            runner2 = runner2.next

        return runner2