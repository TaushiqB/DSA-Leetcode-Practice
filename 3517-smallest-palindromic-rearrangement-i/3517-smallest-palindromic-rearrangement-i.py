class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) <= 2:
            return s

        h = {}
        mid = ""
        left = ""

        for i in range(len(s)):
            if s[i] in h.keys():
                h[s[i]] += 1
            else:
                h[s[i]] = 1

        print(h)
        for i in sorted(h.keys()):
            if h[i] % 2 == 1:
                mid += i
                if h[i]>1:
                    left += i*(h[i]//2)
            else:
                left += i*(h[i]//2)

        return left+mid+left[::-1]
        
        