class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        if v1 == v2 :
            return 0
        n1 = len(v1)-1
        n2 = len(v2)-1
        print(n1, n2)
        min_len= min(n1, n2)
        for i in range(min_len+1):
            print(int(v1[i]) , int(v2[i]) )
            if int(v1[i]) == int(v2[i]):
                continue
            elif int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1

        last_index = i
        if last_index == n1 and last_index == n2:
            return 0
        
        if last_index < n1:
            return 0 if int(''.join(v1[last_index+1:])) == 0 else 1
        if last_index < n2:
            return 0 if int(''.join(v2[last_index+1:])) == 0 else -1
        
        

        # https://leetcode.com/problems/compare-version-numbers/description/