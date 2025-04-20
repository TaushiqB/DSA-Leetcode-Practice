class Solution:
    def reorganizeString(self, s: str) -> str:
        # Brute Force Sorting Method
        # Space Complexity - O(n) Hash Table
        # Time Complexity - O(n +klogk)

        # Use a Hash Table to store chars and their frequencies
        f = {}
        for c in s:  # O(n) To traverse through the string to calculate the ferquency
            f[c] = f.get(c, 0) + 1
        
        # Sort The list based on the frequencies
        c_sort = sorted(f.keys(), key = lambda x: f[x], reverse = True) # O(klogk) to sort the list 
        if f[c_sort[0]] > (len(s)+1)//2:
            return ""
        i = 0
        res=[None]*len(s)
        # Start from the most frequentt characters put them in the even positions
        for c in c_sort:
            for _ in range(f[c]):
                if i >= len(s):
                    i = 1
                res[i] = c
                i+=2
        return "".join(res)