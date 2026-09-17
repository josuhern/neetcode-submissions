class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 0
        for num in nums:
            if num:
                product = product * num
            else:
                count_zero += 1
        
        if count_zero > 1:
            return [0] * len(nums)
        
        result = [0] * len(nums)
        for i, num in enumerate(nums):
            if count_zero:
                if num != 0:
                    result[i] = 0
                else:
                    result[i] = product
            else:
                result[i] = product // num
        return result