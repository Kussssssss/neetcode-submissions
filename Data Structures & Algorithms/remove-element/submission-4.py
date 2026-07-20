class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pivot = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1
        
        return pivot


