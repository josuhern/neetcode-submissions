class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = j = 0
        while j<n:
            nums[i] = nums[j]
            while j<n and nums[i] == nums[j]:
                j+=1
            i+=1
        return i