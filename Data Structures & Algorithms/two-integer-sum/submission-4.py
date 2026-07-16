class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            pivot = target - nums[i]
            for j in range(1, len(nums)):
                if pivot == nums[j] and i != j:
                    return [i, j]