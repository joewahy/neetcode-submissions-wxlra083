class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if len(stack) == 0 and (char == ')' or char == '}' or char == ']'):
                return False
            print(stack)
            if (char == ')' and stack[len(stack) - 1] == '(' ) or (char == '}' and stack[len(stack) - 1] == '{' ) or (char == ']' and stack[len(stack) - 1] == '[' ):
                stack.pop()
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        return False
