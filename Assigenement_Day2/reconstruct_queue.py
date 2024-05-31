class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans
        


        # https://www.youtube.com/watch?v=SthoP5vZ1xk
    # https://walkccc.me/LeetCode/problems/406/#__tabbed_1_3

    # time complexity : O(n2)