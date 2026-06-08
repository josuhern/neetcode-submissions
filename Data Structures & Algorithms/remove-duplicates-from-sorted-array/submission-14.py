class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j=0
        while i<len(nums):
            nums[j]=nums[i]
            while i< len(nums) and nums[j] == nums[i]:
                i+=1
            j+=1




        return j
        