# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

if __name__ == "__main__":
    head_1 = ListNode(3)
    node_1 = ListNode(2)
    node_2 = ListNode(0)
    node_3 = ListNode(-4)

    head_1.next = node_1
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_1

    head_2 = ListNode(1)
    node_1 = ListNode(2)

    head_2.next = node_1

    s = Solution()
    o = s.hasCycle(head_2)
    print(o)

        