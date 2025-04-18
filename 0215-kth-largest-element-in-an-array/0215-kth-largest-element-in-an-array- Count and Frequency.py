class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Counting and Sorting Technique
        min_val = min(nums)
        max_val = max(nums)

        frq = [0]*(max_val - min_val + 1)
        for i in nums:
            frq[i - min_val] += 1
        
        for i in range(len(frq) - 1, -1,-1):
            k -= frq[i] 

            if k <= 0:
                return i + min_val