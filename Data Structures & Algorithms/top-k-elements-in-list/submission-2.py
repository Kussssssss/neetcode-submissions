class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}

        for n in nums:
            maps[n] = maps.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in maps.items():
            buckets[c].append(n)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
            