def longestSubstring(str1):
    l = 0
    result = 0
    dummy = set()
    for r in range(len(str1)):
        if str1[r] in dummy:
            dummy.remove(str1[l])
            l +=1
        dummy.add(str1[r])
        result = max(result,r-l +1)
    
    return result


str1 = 'pwwkew'
print(longestSubstring(str1))

