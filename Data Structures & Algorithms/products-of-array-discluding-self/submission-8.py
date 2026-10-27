class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        zeros = 0
        multiple = 1
        
        for num in nums:
            if num != 0:
                multiple *= num
            else:
                zeros += 1
        
        for num in nums:
            if zeros == 0:
                result.append(multiple // num)
            elif num == 0 and zeros == 1:
                result.append(multiple)
            else:
                result.append(0)
        
        return result