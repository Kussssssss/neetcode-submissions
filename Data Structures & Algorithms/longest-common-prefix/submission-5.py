class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        char = ""
        for i in range(len(strs[0])):
            char = char + strs[0][i]
            for str in strs:
                if i >= len(str) or char[i] != str[i]:
                    return char[:-1]
        return char