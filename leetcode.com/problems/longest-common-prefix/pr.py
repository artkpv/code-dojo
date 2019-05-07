#!python3
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        i = 0
        while True:
            are_same = True
            # check that all are the same at i-th
            for j in range(1, len(strs)):
                a = strs[j-1]
                b = strs[j]
                if (i >= min(len(a), len(b))
                        or a[i] != b[i]):
                    are_same = False
                    break
            if not are_same:
                i -= 1
                break
            i += 1
        return strs[0][:i+1]


