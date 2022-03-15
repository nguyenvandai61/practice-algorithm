class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in s1:
            s1_count[ord(i) - ord('a')] += 1
        for i in s2[:len(s1)]:
            s2_count[ord(i) - ord('a')] += 1
        print(s1_count, s2_count)
        if s1_count == s2_count:
            return True
        for i in range(len(s2) - len(s1)):
            print(s2[i])
            s2_count[ord(s2[i]) - ord('a')] -= 1
            s2_count[ord(s2[i + len(s1)]) - ord('a')] += 1
            if s1_count == s2_count:
                return True
        return False
      
if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))
    print(s.checkInclusion("ab", "eidboaoo"))