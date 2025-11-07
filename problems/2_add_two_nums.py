from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = output = None
        carry_over = False

        if l1.val == 0 and l1.next == None:
            return l2
        
        if l2.val == 0 and l2.next == None:
            return l1

        while l1 != None and l2 != None:
            extra = 0
            if carry_over:
                extra = 1
                carry_over = False
            
            val = l1.val + l2.val + extra
            if val >= 10:
                carry_over = True
                val = val % 10
            
            new_node = ListNode(val=val, next=None)
            l1 = l1.next
            l2 = l2.next

            if l3 == None:
                l3 = output = new_node
            else:
                l3.next = new_node
                l3 = l3.next
        
        if l1 != None and l2 == None:
            while l1 != None:
                extra = 0
                if carry_over:
                    extra = 1
                    carry_over = False
                
                val = l1.val + extra
                if val >= 10:
                    carry_over = True
                    val = val % 10
                
                new_node = ListNode(val=val, next=None)
                l1 = l1.next

                l3.next = new_node
                l3 = l3.next

        if l2 != None and l1 == None:
            while l2 != None:
                extra = 0
                if carry_over:
                    extra = 1
                    carry_over = False
                
                val = l2.val + extra
                if val >= 10:
                    carry_over = True
                    val = val % 10
                
                new_node = ListNode(val=val, next=None)
                l2 = l2.next

                l3.next = new_node
                l3 = l3.next
            
        if carry_over:
            val = 1
            new_node = ListNode(val=val, next=None)
            l3.next = new_node
        
        return output


if __name__ == "__main__":
    l1_1 = [2,4,3]
    l2_1 = [5,6,4]
    l1_2 = [0]
    l2_2 = [0]
    l1_3 = [9,9,9,9,9,9,9]
    l2_3 = [9,9,9,9]

    s = Solution()
    o = s.addTwoNumbers(l1_3, l2_3)
    print(o)
