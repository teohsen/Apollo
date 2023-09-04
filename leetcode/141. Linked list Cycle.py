from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Hash Table Method
        """
        seen_nodes = set()
        cur_node = head
        while cur_node:
            # if cur_node in seen_nodes:
            if seen_nodes.__contains__(cur_node):
                return True
            seen_nodes.add(cur_node)
            cur_node = cur_node.next

        return False
