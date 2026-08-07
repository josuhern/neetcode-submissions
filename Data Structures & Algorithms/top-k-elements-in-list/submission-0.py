from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        for x in nums:
            num_dict[x] += 1
        result = []
        for i in range(k):
            max_num = -1
            new_max = max_num
            aux = -1
            for val, frequence in num_dict.items():
                new_max = max(frequence, max_num)
                if new_max != max_num:
                    max_num = new_max
                    aux = val
            result.append(aux)
            num_dict.pop(aux)
        return result
                
