class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n

        def fibo(i: int) -> int:
            if i >= n:
                return i == n
            if dp[i] != -1:
                return dp[i]
            dp[i] = fibo(i+1) + fibo(i+2)
            return dp[i]
        
        return fibo(0)
            