class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def recursion(curr):
            if curr == n:
                return 1
            if curr > n:
                return 0
            if curr in memo:
                return memo[curr]
            
            memo[curr] = recursion(curr + 1) + recursion(curr + 2)
            return memo[curr]
            
        return recursion(0)