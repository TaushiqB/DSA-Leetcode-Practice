class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Frequency mean hash map
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        
        m = max(freq.values())

        s = 0

        for i in freq.values():
            if m == i:
                s+=m
        
        return s