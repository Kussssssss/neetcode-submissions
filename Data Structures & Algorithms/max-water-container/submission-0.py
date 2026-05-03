class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxium = 0

        while l < r:
            maxium = max(maxium, (r-l)*min(heights[l], heights[r]))
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        
        return maxium
            
            