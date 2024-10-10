
def longestValidParentheses(s: str) -> int:
    if not s:
        return 0
    arr = [0] * len(s)
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append([s[i], i])
        elif s[i] == ')':
            if stack and stack[-1][0] == '(':
                ele, key = stack.pop()
                arr[i]=1
                arr[key]=1
    print(arr)
    count = 0
    max_len = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count = 0
        elif arr[i] == 1:
            count+=1
            print(max_len)
            max_len = max(max_len, count)
    return max_len

        
        