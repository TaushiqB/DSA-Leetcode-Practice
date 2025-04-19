class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Hash Table
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
        t = []
        for key in h:
            t.append([h[key], key])
        t = sorted(t, reverse = True)
        return [t[i][1] for i in range(k)]

        
        