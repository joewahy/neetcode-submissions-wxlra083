class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        result = []
        for i in nums:
            if i not in hash:
                hash[i] = 0
            hash[i] += 1

        for i in range(k):
            biggest_key = max(hash, key = hash.get)
            result.append(biggest_key)
            hash.pop(biggest_key)


        return result


        