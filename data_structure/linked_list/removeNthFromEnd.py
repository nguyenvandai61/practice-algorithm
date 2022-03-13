# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=head
        l=0
        while p:
            l+=1    
            p=p.next
            
        if l==n:
            return head.next
          
        k=l-n-1
        p=head
        while k and p.next:
            k-=1
            p=p.next
        p.next=p.next.next
        self.print_list(head)
        return head
      
    def print_list(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val, end=' ')
            head = head.next
        print()
        
if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(s.removeNthFromEnd(head, 2))
    head = ListNode(1)
    print(s.removeNthFromEnd(head, 1))