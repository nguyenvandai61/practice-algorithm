from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotate_right(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        nt = head
        a = []
        length = 0
        while nt:
            length+=1
            a.append(nt.val)
            nt = nt.next
        k %= length
        if k == 0:
            return head
        print(a[-k:])
        print(a[:-k])
        print('k', k)
        new_a =a[-k:] + a[:-k]
        print('new_a', new_a)
        nt = ListNode(new_a[len(new_a)-1])
        i = 1
        while i<len(new_a):
            val = new_a[len(new_a)-1-i]
            nt = ListNode(val, nt)
            i+=1
        return nt
    
    def print_list(self, head: Optional[ListNode]):
        nt = head
        print('[', end='')
        while nt:
            print(nt.val, end=', ')
            nt = nt.next
        print(']')

if __name__ == '__main__':
    s = Solution()
    # head = ListNode(1, ListNode(3, ListNode(5, ListNode(2, ListNode(4)))))
    head = ListNode(1, ListNode(2))
    head1 = s.rotate_right(head, 1)
    s.print_list(head1)