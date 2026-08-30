class Solution:
    def isValid(self, s: str) -> bool:
        start = 0
        last = len(s)-1
        stack = []
        while start <= last:
            if s[start] == "(":
                stack.append("(")
            elif s[start] == "[":
                stack.append("[")
            elif s[start] == "{":
                stack.append("{")
            elif s[start] == ")":
                if stack == []:
                    return False
                elif stack[-1] != "(":
                    return False
                stack.pop()
            elif s[start] == "]":
                if stack == []:
                    return False
                elif stack[-1] != "[":
                    return False
                stack.pop()
            elif s[start] == "}":
                if stack == []:
                    return False
                elif stack[-1] != "{":
                    return False
                stack.pop()
            start += 1
        
        return stack == []