class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            enconded_add = f"{len(word)}#{word}"
            encoded.append(enconded_add)
        result = "".join(encoded)
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        s_len = len(s)
        i = 0
        while i<s_len:
            j = i
            while s[j] != "#":
                j+=1
            addition = int(s[i:j])
            start = j+1
            end = start+addition
            i = end
            word = s[start:end]
            result.append(word)
        return result



