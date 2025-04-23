class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy Algorithm try the max jump
        # Time complexity: O(n)
        # Space complexity: O(1)

        maxInd = 0
        for i in range(len(nums)):
            if i > maxInd:
                return False
            if maxInd > len(nums):
                break
            maxInd = max(maxInd, i+nums[i])
        return True
