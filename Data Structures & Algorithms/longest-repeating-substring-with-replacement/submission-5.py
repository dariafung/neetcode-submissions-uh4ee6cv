class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        mfreq = 0
        res = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            mfreq = max(mfreq, count[s[r]])

            if r - l + 1 - mfreq > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)

        return res