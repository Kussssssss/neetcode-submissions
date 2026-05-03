class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_sets = set(nums)
        longest = 0

        for n in num_sets:
            if n-1 not in num_sets:
                length = 1
                while n+length in num_sets:
                    length+=1
                longest = max(longest, length)
        
        return longest
            