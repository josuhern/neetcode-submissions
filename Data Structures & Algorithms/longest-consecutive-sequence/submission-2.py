class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        count = 1
        for current in numSet:
            if (current-1) not in numSet:
                count = 1
                while current + count in numSet:
                    count+=1
                longest = max(count, longest)
        return longest