class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maps = {}
        for i in nums:
            maps[i] = maps.get(i, 0) + 1

        max = 0
        pivot = 0
        for key, value in maps.items():
            if value >= max:
                max = value
                pivot = key
        
        return pivot
            
