# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr and curr.next:
            nextNode = curr.next
            prev.next = nextNode
            curr.next = nextNode.next
            nextNode.next = curr

            prev = curr
            curr = curr.next
        return dummy.next
