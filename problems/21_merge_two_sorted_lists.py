from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        output_node = None
        merged_list = None
        
        while list1 is not None and list2 is not None:
            if merged_list is None:
                if list1.val <= list2.val:
                    merged_list = ListNode(list1.val)
                    output_node = merged_list
                    list1 = list1.next
                else:
                    merged_list = ListNode(list2.val)
                    output_node = merged_list
                    list2 = list2.next
            else:
                if list1.val <= list2.val:
                    merged_list.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    merged_list.next = ListNode(list2.val)
                    list2 = list2.next
                merged_list = merged_list.next

        if list1 is None:
            merged_list.next = list2

        if list2 is None:
            merged_list.next = list1

        return output_node


if __name__ == "__main__":
    tc_1 = ""
    tc_2 = ""

    s = Solution()
    o = s.problem_name(tc_1)
    print(o)

