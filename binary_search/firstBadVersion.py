# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def first_bad_version(self, n: int) -> int:
        p = 0
        q = n
        piv = (p+q)//2
        while p<=q:
            if isBadVersion(piv) and not isBadVersion(piv-1):
                return piv
            elif isBadVersion(piv) and isBadVersion(piv-1):
                q = piv-1
                piv = (p+q)//2
            else:
                p = piv+1
                piv = (p+q)//2
        return -1