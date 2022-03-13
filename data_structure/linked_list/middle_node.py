# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p = head
        l = 0
        while p:
            l += 1
            p = p.next
        
        half_l = l // 2
        while half_l:
            head = head.next
            half_l -= 1
        s.print_list(head)
        return head

    def print_list(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val, end=' ')
            head = head.next
        print()
if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(s.middleNode(head))