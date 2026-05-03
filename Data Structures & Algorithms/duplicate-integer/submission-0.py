class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = {}

        for n in nums:
            maps[n] = maps.get(n, 0) + 1

        for _, c in maps.items():
            if c > 1:
                return True
        
        return False