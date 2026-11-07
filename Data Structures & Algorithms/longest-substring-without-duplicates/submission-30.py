class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        last_seen = {}
        longest = 0
        start = 0
        for i, char in enumerate(s):
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            last_seen[char] = i
            longest = max(i - start + 1, longest)
        return longest