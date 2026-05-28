class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Sliding window solution

        currsum = nums[0]
        maxsum = nums[0]

        for i in range(1, len(nums)):
            
            if currsum<0:
                currsum = 0
            
            currsum+=nums[i]
            maxsum = max(maxsum, currsum)

        return maxsum