# defaultdict returns not present for keys which are not present unlikely dict ehich throws key error
from collections import defaultdict

def group_anagrams(s1):
    d = defaultdict(list)
    for s in s1:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] +=1
        d[tuple(count)].append(s)
    return list(d.values())


str1= ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(str1))