class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        # Count the number of sorted numbers   
        # Time Complexity - O(n)
        # Space Complexity - O(1)
        ans = 0
        p = -1
        for num in nums:
            if num >= p:
                p = num
                ans += 1
        return ans