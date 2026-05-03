class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_t = [0] * 26
        counts_s = [0] * 26

        for c in s:
            counts_s[ord(c) - ord("a")] += 1

        for c in t:
            counts_t[ord(c) - ord("a")] += 1

        return counts_t == counts_s