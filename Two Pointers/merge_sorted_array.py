class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #  approach 1
        p2 = n - 1
        p1 = m - 1
        ind = m+ n -1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[ind] = nums1[p1]
                p1 -=1
            else:
                nums1[ind] = nums2[p2]
                p2 -=1
            ind -=1
            
        nums1[:p2+1] = nums2[:p2+1]
        #  time complexity : O(n+m)
        # space complexity : O(1)
            

        



            
            



        
        # https://leetcode.com/problems/merge-sorted-array/