class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort first to keep big numbers back, Mostly transform to big numbers

        l = 0
        r = 0
        total = 0
        res = 0
        
        # Simple Sliding window

        for r in range(len(nums)):
            total += nums[r]
            while (r - l + 1)*nums[r] - total > k:
                # Formula means , imagine we take a right ( bigger) Number as all other numbers want to transform as
                # Basically finding the difference between the largest number selected and the other numbers within the window
                total -= nums[l]
                l += 1

            res = max(res, r - l + 1)

        return res