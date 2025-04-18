class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Presum and Hash Map Optimal Solution
        h = {}
        count = 0
        h[0] = 1
        presum = 0
        for i in range(len(nums)):
            presum += nums[i]
            remove = presum - k
            if remove in h:
                count += h[remove]
            if presum in h:
                h[presum] += 1
            else:
                h[presum] = 1
        return count
