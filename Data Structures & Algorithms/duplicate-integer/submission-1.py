class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = set()

        for i in nums:
            if i not in maps:
                maps.add(i)
            else:
                return True
            
        return False