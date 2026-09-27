class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def recursive(opened, closed, current, so_far):
            if opened == n and closed == n:
                so_far.append(current)
                return
            if opened < n:
                recursive(opened + 1, closed, current + "(", so_far)
            if closed < opened:
                recursive(opened, closed + 1, current + ")", so_far)

        result = []
        recursive(0, 0, "", result)
        return result