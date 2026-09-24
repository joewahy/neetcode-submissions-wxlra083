class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append(index)
            else:
                while(stack and temperatures[stack[len(stack) - 1]] < temp):
                    popped = stack.pop()
                    result[popped] = index - popped
                stack.append(index)
        while(stack):
            result[stack.pop()] = 0
        return result