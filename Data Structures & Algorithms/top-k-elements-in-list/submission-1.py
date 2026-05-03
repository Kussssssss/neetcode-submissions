class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}

        for n in nums:
            maps[n] = maps.get(n, 0) + 1
        
        sorted_item = sorted(maps.items(), key=lambda x: x[1], reverse=True)
        
        return [item[0] for item in sorted_item[:k]]
            