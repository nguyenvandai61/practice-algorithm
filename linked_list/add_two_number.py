# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = l1.val
        nt = l1.next
        i = 0
        while nt:
            i += 1
            print(nt.val)
            r1+=nt.val * pow(10, i)
            nt = nt.next
            
        print(r1)
        r2 = l2.val
        nt = l2.next
        i = 0
        while nt:
            i += 1
            print(nt.val)
            r2+=nt.val * pow(10, i)
            nt = nt.next
        print(r2)
        
        r = r1+r2
        
        # split the number into digits
        digits = []
        while r:
            digits.append(r%10)
            r = r//10
        
        if not digits:
          digits = [0]
          
        print(digits)
        i = len(digits)-1 
        nt = ListNode(digits[i])
        while i > 0:
            i -= 1
            nt = ListNode(digits[i], nt)
        self.print_list(nt)
        return nt    
        
        # print all values
    def print_list(self, l: Optional[ListNode]):
        print('[', end='')
        while l:
            print(l.val, end=', ')
            l = l.next
        print(']')
    
    def test(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        self.print_list(self.add_two_numbers(l1, l2))
    
    def test2(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        self.print_list(self.add_two_numbers(l1, l2))
        
if __name__ == "__main__":
    s = Solution()
    s.test()
    s.test2()