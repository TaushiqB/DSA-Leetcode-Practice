class Solution:
    def jump(self, nums):
        # Dynamic Programming with Memoization
        # Time Complexity O(n^2)
        # Space Complexity O(n)
        dp = {i:10001 for i in range(len(nums))}
        
        def ans(pos):
            if pos >= len(nums)-1:
                return 0
            if dp[pos] != 10001: 
                return dp[pos]          # Here the Repitition Stops
            for i in range(1, nums[pos]+1):
                dp[pos] = min(dp[pos], 1 + ans(pos+i))
            return dp[pos]
        return ans(0)