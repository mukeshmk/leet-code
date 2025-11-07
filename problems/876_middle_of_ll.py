
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        mid = head
        while head.next != None:
            if l % 2 == 1:
                mid = mid.next
            l += 1
            head = head.next
        
        if l % 2 == 1:
            mid = mid.next

        return mid

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

    s = Solution()
    o = s.numberOfSteps(head)
    print(o)
