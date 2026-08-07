class Solution:
    def generateKey(self, st:str)-> str:
        key = sorted(st)
        result = ''.join(key)
        return result
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        #generate key
        for s in strs:
            key = self.generateKey(s)
            hash_map[key].append(s)
        #conver the map to a list
        return list(hash_map.values())