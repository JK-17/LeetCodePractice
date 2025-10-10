# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head:
            return True

        # find middle using slow/fast pointer
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # use slow pointer and reverse
        prev = None
        while slow:
            temp_node = slow.next
            slow.next = prev
            prev = slow
            slow = temp_node

        
        # compare left and right step by step
        left, right = head, prev

        while left and right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next

        return True



            
        