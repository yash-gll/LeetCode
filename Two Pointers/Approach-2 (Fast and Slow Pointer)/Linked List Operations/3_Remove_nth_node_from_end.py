'''Given the head of a linked list, remove the nth node from the end of the list and return its head.'''
'''
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(n):
            slow = slow.next
        while slow:
            slow = slow.next
            if slow:
                fast = fast.next
        fast.next = fast.next.next
        return dummy.next