class Solution:
    def climbStairs(self, n: int) -> int:
        step1, step2 = 1, 1

        for _ in range(n-1):
            temp = step1 + step2
            step1 = step2
            step2 = temp
        
        return step2

            