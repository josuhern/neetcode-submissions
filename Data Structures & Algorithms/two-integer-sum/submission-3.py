class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        n = len(nums)
        dict_nums = {}
        while i < n:
            while j < n:
                if nums[i]+nums[j] == target:
                    return [i,j]
                j+=1
            i+=1
            j=i+1
        return []