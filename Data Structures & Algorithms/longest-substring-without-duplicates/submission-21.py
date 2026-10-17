class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        highest = 0
        window = 0
        for i in range(len(s)):
            if s[i] in last_seen and last_seen[s[i]] >= window:
                highest = max(highest, i - window)
                window = last_seen[s[i]] + 1
            last_seen[s[i]] = i
        
        highest = max(highest, len(s) - window)

        return highest
        