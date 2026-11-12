class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = {}
        for char in t:
            if char not in seen:
                seen[char] = 0
            seen[char] += 1
        
        result = ""
        so_far = ""
        for i, char in enumerate(s):
            so_far += char
            if char in seen:
                seen[char] -= 1


            if all(v <= 0 for v in seen.values()):
                while all(v <= 0 for v in seen.values()):
                    if so_far[0] not in seen:
                        so_far = so_far[1:]
                    else:
                        if len(result) == 0 or len(so_far) < len(result):
                            result = so_far
                        seen[so_far[0]] += 1
                        so_far = so_far[1:]
        
        return result
