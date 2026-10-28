class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        prev = nums[0]
        result = 0
        for num in nums:
            if prev == num:
                continue
            if num != prev + 1:
                result = max(result, count)
                count = 0
            prev = num
            count += 1

        return max(result, count)