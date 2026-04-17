# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
 

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2
        return dummy.next
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # Split the linked list into halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        # Sort each half
        left_half = self.sortList(head)
        right_half = self.sortList(mid)
        
        # Merge the sorted halves
        return self.merge(left_half, right_half)