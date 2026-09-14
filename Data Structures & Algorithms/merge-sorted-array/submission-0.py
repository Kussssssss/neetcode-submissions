class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l, r, pivot = m-1, n-1, m+n-1 

        while l > -1 and r > -1:
            if nums1[l] > nums2[r]:
                nums1[pivot] = nums1[l]
                l -= 1
            else:
                nums1[pivot] = nums2[r]
                r -= 1
            
            pivot -= 1
        
        while l > -1:
            nums1[pivot] = nums1[l]
            l -= 1
            pivot -= 1

        while r > -1:
            nums1[pivot] = nums2[r]
            r -= 1
            pivot -= 1
        
        
        

        



        