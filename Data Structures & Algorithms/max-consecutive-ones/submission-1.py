class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max, last_max = 0, 0
        for i in nums:
            if i == 1:
                curr_max += 1
            elif i == 0:
                if last_max <= curr_max:
                    last_max = curr_max
                curr_max = 0
        
        if curr_max > last_max:
            return curr_max
        else:
            return last_max

