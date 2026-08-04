class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aux = set()
        for x in nums:
            if x in aux:
                return True
            else:
                aux.add(x)
        return False
        