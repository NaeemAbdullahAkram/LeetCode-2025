class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        prev = dummyNode
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                node = current
                while node and node.val == current.val:
                    node = node.next
                current = node
                prev.next = node
            else:
                prev = current
                current = current.next
        
        return dummyNode.next