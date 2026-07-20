class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            if nums[l] == val:
                r -= 1
                nums[l] = nums[r]
            else:
                l += 1        

        return r


