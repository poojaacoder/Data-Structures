class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = 0 
        right = len(people) -1
        boats = 0
        people.sort()
        while left <= right:
            remain = limit - people[right]
            right -=1
            if people[left] <= remain:
                left +=1
            boats +=1
        return boats





        """

        """
        # https://leetcode.com/problems/boats-to-save-people/