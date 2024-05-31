class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0
        
        temp = nums[0]
        for i in range(n):
            if nums[i] > 0:
                nums[nums[i]% n-1] += n

        if nums[0] == temp: return 1
        for i in range(n):
            if nums[i] // n == 0:
                return i+1
            
        return n



# TypeError: None is not valid value for the expected return type integer
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     raise TypeError(str(ret) + " is not valid value for the expected return type integer");
# Line 33 in _driver (Solution.py)
#     _driver()
# Line 40 in <module> (Solution.py)
# During handling of the above exception, another exception occurred:
# TypeError: '<' not supported between instances of 'int' and 'NoneType'
# Line 14 in _serialize_int (./python3/__serializer__.py)
# Line 63 in _serialize (./python3/__serializer__.py)
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     out = ser._serialize(ret, 'integer')
# Line 31 in _driver (Solution.py)
        
        # https://leetcode.com/problems/first-missing-positive/submissions/1262070947/