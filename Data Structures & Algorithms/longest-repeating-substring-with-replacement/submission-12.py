class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        chars = {}

        for right in range(len(s)):
            if s[right] not in chars:
                chars[s[right]] = 0
            chars[s[right]] += 1
            if (right - left + 1) - max(chars.values()) > k:
                chars[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest