class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Two Pointer and Greedy
        l = len(g)-1
        r = len(s)-1
        g = sorted(g)
        s = sorted(s)
        while l!=-1 and r!=-1:
            if g[l] <= s[r]:
                r-=1
            l-=1
        return len(s)-r-1