# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        left = dummyNode
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummyNode.next

#         My code
#         currentNode = head
#         length = 1
#         while currentNode.next != None:
#             length += 1
#             currentNode = currentNode.next

#         currentNode = head
#         i = 0
#         while i < length - n - 1:
#             i += 1
#             currentNode = currentNode.next

#         if i == 0:
#             currentNode = currentNode.next
#         else:
#             currentNode.next = currentNode.next.next
#         return head
