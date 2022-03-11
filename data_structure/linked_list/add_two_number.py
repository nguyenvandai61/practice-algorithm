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
    def add_two_numbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        is_remembered = False
        nt = None
        res = []
        while n1 or n2:
            a = n1.val if n1 else 0
            b = n2.val if n2 else 0
            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None
            r = a+b
                
            if is_remembered:
                r += 1
                is_remembered = False
            if r > 9:
                r = r%10
                is_remembered = True
            
            res.append(r)
        
        if is_remembered:
            res.append(1)
        print('reverse:', res[::-1])
        for i in res[::-1]:
            nt = ListNode(i, nt)
        return nt

    def print_list(self, l: Optional[ListNode]):
        print('[', end='')
        while l:
            print(l.val, end=', ')
            l = l.next
        print(']')
    
    def test(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        self.print_list(self.add_two_numbers2(l1, l2))
    
    def test2(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        l2 = ListNode(9, ListNode(9, ListNode(9)))
        self.print_list(self.add_two_numbers2(l1, l2))
        
if __name__ == "__main__":
    s = Solution()
    s.test()
    s.test2()