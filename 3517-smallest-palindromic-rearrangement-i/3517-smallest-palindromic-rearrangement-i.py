class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 2:
            return s
        m = n//2
        st = sorted(s[:n//2])
        ts = st[::-1]
        if n % 2 == 1:
            st += s[m]

        return ''.join(st + ts)
                    