# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 

# Follow-up: Can you solve the problem in O(1) extra memory space?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverse(self, head: ListNode, tail: ListNode) -> (ListNode, ListNode):
        prev = tail.next
        curr = head

        while prev != tail:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return tail, head
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            next_group = tail.next
            head, tail = self.reverse(prev.next, tail)

            prev.next = head
            tail.next = next_group
            prev = tail