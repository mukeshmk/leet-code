from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
                



if __name__ == "__main__":
    head_1 = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))))
    val_1 = 6
    head_2 = None
    val_2 = 1
    head_3 = ListNode(7, ListNode(7, ListNode(7, ListNode(7, None))))
    val_3 = 7

    s = Solution()
    o = s.removeElements(head_3, val_3)
    while o is not None:
        print(o.val)
        o = o.next
        