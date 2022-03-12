"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copy_random_list(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        p = Node(head.val)
        q = p
        r = head
        while r.next:
            q.next = Node(r.next.val)
            q = q.next
            r = r.next
        r = head
        p2 = p
        while r:
            if r.random:
                temp = head
                temp2 = p
                while temp:
                    if id(temp) == id(r.random):
                        p2.random = temp2
                        break
                    temp = temp.next
                    temp2 = temp2.next
            r = r.next
            p2 = p2.next
        return p
        
    def copy_random_list2(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        self.print_list(head)
        p2 = Node(head.val)
        p = p2
        r = head
        d = { r: p }
        while r:
            print('id(r)', id(r))
            p.next = Node(r.val)
            r = r.next
            p = p.next
            d[r] = p
        
        r = head
        p = p2
        while r:
            print(id(r), end=' ')
            if r.random:
                p.random = d[r.random]
            r = r.next
            p = p.next
            
        print(p.val)
        print('id p', id(p))
        print('id p2', id(p2))
        self.print_list(p2)


   
    def print_list(self, head: Optional[Node]):
        p = head
        print('------------------------')
        while p:
            print(id(p), end=' ')
            print(f'val{p.val}', end='-')
            print(f'nextVal{p.next.val if p.next else "None"}', end='-')
            print(id(p.random) if p.random else None, end='    ')
            print()
            p = p.next
        print()
        
        
if __name__=='__main__':
    s = Solution()
    n0 = Node(7, None, None)
    n1 = Node(13, None, None)
    n2 = Node(11, None, None)
    n3 = Node(10, None, None)
    n4 = Node(1, None, None)
    
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    n1.random = n0
    n2.random = n4
    n3.random = n2
    n4.random = n0
    s.print_list(s.copy_random_list2(n0))