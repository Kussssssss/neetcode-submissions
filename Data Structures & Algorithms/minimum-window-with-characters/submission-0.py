class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        need_types = len(need)       # number of distinct chars we must satisfy
        formed = 0                  # number of distinct chars currently satisfied

        l = 0
        best_len = float("inf")
        best_l = 0

        for r, ch in enumerate(s):
            if ch in need:
                have[ch] = have.get(ch, 0) + 1
                if have[ch] == need[ch]:
                    formed += 1

            # try shrink while valid
            while formed == need_types:
                window_len = r - l + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l = l

                left_ch = s[l]
                if left_ch in need:
                    have[left_ch] -= 1
                    if have[left_ch] < need[left_ch]:
                        formed -= 1
                l += 1

        if best_len == float("inf"):
            return ""
        return s[best_l: best_l + best_len]
