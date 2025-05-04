class Solution:
    def jump(self, nums):
        # Iterative Dynamic Programming with Memoization
        # Time Complexity O(n^2)
        # Space Complexity O(n)
        n = len(nums)
        dp = {i:10001 for i in range(n)}
        dp[n-1] = 0
        for i in range(n-2,  -1, -1):
            for j in range(1, nums[i]+1):
                dp[i] = min(dp[i], 1 + dp[min(n-1, i+j)])
        return dp[0]