class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strings = ""

        for s in strs:
            encoded_strings += str(len(s)) + "#" + s

        return encoded_strings


    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            
            while str(s[j]) != '#':
                j += 1
            
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        
        return res
