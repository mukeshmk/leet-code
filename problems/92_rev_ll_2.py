from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        node = head
        
        while node:
            if i == left:
                pass


if __name__ == "__main__":
    head_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    left_1 = 2
    right_1 = 4

    s = Solution()
    o = s.reverseBetween(head_1, left_1, right_1)
    while o is not None:
        print(o.val)
        o = o.next
        