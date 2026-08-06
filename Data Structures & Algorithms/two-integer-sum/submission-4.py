class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_n = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in dict_n:
                return [dict_n[complement], i]
            dict_n[n] = i
        return []