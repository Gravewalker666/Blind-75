class Solution:
    def getCorrespondingClosingBraket(self, braket: str) -> str:
        if (braket == '('):
            return ')'
        if (braket == '{'):
            return "}"
        if (braket == '['):
            return ']'

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == "[":
                stack.append(c)
            elif c == ')' or c == '}' or c == "]":
                if (stack == []): return False
                if not (self.getCorrespondingClosingBraket(stack.pop()) == c):
                    return False
        if (stack != []):
            return False
        return True
