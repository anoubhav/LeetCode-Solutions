class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        ans = ''
        for char, freq in c.most_common():
            ans += char*freq
        return ans
        