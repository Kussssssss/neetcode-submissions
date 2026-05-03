class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            p = target - nums[i]
            for j in range(len(nums)-1):
                j += 1
                if nums[j] == p and j != i:
                    return [i, j]