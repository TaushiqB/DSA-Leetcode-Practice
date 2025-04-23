class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy Solution
        # Start from the behind and move the goal as close to us as possible
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        g = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= g:
                g = i

        return True if g == 0 else False