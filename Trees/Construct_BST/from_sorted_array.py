class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build(left, right):
            while left < right:
                mid = (left+right) // 2
                return TreeNode(nums[mid], build(left, mid), build(mid+1, right))

    
        return build(0, len(nums))
    
    # https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/