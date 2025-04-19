class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # set method
        return len(set(nums) - {0})
        