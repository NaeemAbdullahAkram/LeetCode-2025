# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = [] # holds numbers than x
        right = [] # holds numbers greater than x

        temp = head
        while temp:
            if temp.val < x:
                left.append(temp.val)
            else:
                right.append(temp.val)
            # end if
            temp = temp.next
        # end while
        
        # overwrite the values in the order
        temp = head
        i = 0
        while i < len(left):
            temp.val = left[i]
            temp = temp.next
            i += 1
        # end while
        i = 0
        while i < len(right):
            temp.val = right[i]
            temp = temp.next
            i += 1
        # end while
        
        return head