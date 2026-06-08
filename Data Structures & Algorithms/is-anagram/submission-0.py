class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sHash = defaultdict(int)
            for x in s:
                sHash[x] += 1
            for y in t:
                sHash[y] -= 1
            for z in sHash.values():
                if z !=0:
                    return False
            return True

        else: return False