class Solution:
    def calculate(self, s: str) -> int:
        output = cur = 0
        sign = 1
        stack = []

        for c in s:
            # digit
            print()
            if c.isdigit():
                cur = cur* 10 + int(c)
            # +-
            elif c in '+-':
                output += (cur *sign)
                cur = 0
                sign = -1 if c == '-' else 1
            # (
            elif c == '(':
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif c == ')':
                output += (cur*sign)
                output *= stack.pop()
                output += stack.pop()
                cur = 0
        return output + (cur*sign)

            # )
        

        # https://leetcode.com/problems/basic-calculator/