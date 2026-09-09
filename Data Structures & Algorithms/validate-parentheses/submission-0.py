class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            else:
                if not stack:
                    return False
                current = stack.pop()
                if current == "(":
                    if i != ")":
                        return False
                if current == "[":
                    if i != "]":
                        return False
                if current == "{":
                    if i != "}":
                        return False
        if stack:
            return False
        else:
            return True