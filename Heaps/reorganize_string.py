class Solution:
    def reorganizeString(self, s: str) -> str:

        # need to revisit 
        count = collections.Counter(s)
        if max(count.values()) > (len(s) + 1) // 2:
            return ''
        ans = []
        maxHeap = [(-freq, c) for c, freq in count.items()]
        heapq.heapify(maxHeap)
        print(maxHeap)
        prevFreq = 0
        prevChar = '@'

        while maxHeap:
            print(ans)
            freq, c = heapq.heappop(maxHeap)
            ans.append(c)
            if prevFreq < 0:
                heapq.heappush(maxHeap, (prevFreq, prevChar))
            prevFreq = freq + 1
            prevChar = c

        return ''.join(ans)

        # https://leetcode.com/problems/reorganize-string/description/