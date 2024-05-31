class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) //2
        temp2 = set()
        temp2.add(0)
        temp2.add(nums[-1])
        for i in range(len(nums)-2, -1, -1):
            temp = set()
            for n in temp2:
                s = n + nums[i]
                temp.add(n)
                if s == target : return True
                if s not in temp:
                    temp.add(s)
            temp2 = temp
                
        return False


# https://leetcode.com/problems/partition-equal-subset-sum/
# https://www.youtube.com/watch?v=IsvocB5BJhw&t=302s
                






        
                




        