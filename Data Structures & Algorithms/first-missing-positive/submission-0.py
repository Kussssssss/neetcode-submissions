class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            tar = abs(nums[i])
            if 1 <= tar <= len(nums):
                if nums[tar - 1] > 0:
                    nums[tar - 1] *= -1
                elif nums[tar - 1] == 0:
                    nums[tar - 1] = -1 * (len(nums) + 1)
                
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        return len(nums) + 1
        
