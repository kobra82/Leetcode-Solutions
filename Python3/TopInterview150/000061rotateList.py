# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # Find the length of the linked list and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Connect the tail to the head to make it circular
        tail.next = head

        # Calculate the effective rotations needed
        k = k % length
        steps_to_new_head = length - k

        # Find the new tail and new head
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        # Break the circular link
        new_tail.next = None

        return new_head