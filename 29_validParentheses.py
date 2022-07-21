class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char in ["(", "[","{"]:
                stack.append(char)
            else:
                # stack can not empty now.
                if not stack:
                    return False
                top_char = stack.pop()
                if char == ")" and top_char != "(":
                    return False
                if char == "]" and top_char != "[":
                    return False
                if char == "}" and top_char != "{":
                    return False
        if stack:
            return False
        else:
            return True
s = "([)]"
iV = Solution()
rel = iV.isValid(s)
print("rel = ", rel)