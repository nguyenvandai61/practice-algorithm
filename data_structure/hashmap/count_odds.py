class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1) // 2 if low % 2 == 1 else (high - low + 1) // 2