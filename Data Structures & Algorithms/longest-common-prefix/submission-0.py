class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ''
        strs = sorted(list(strs))
        first, last = strs[0], strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return string
            else:
                string += first[i]
        return string
