class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 2 * len(nums)
        result = [0] * n
        for i in range(len(nums)):
            result[i] = nums[i]
            result[i+len(nums)] = nums[i]

        return result