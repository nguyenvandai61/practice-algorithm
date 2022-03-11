from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        max_val = max(salary)
        min_val = min(salary)
        print(max_val)
        print(min_val)
        salary[:] = filter(lambda x: x != max_val and x != min_val, salary)
        return sum(salary) // len(salary)
        
if __name__ == '__main__':
    s = Solution()
    salary = [4000,3000,1000,2000]
    print(s.average(salary))