# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ls = prev = ListNode(0)
        ls.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                prev.next = head
            else:
                prev = prev.next
                head = head.next
                    
        return ls.next
      
    def print_list(self, head: Optional[ListNode]):
        nt = head
        print('[')
        while nt:
            print(nt.val)
            nt = nt.next
        print()
        