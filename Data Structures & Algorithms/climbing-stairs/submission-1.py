from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0

        @cache
        def recursion(curr):
            count = 0
            if curr == n:
                return 1
            if curr < n:
                count += recursion(curr + 1)
                count += recursion(curr + 2)
            return count
        return recursion(0)