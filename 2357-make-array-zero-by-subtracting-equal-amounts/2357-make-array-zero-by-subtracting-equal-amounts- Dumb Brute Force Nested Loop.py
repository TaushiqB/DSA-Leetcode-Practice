class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Nested loop brute force
        c = 0
        while sum(nums) != 0:
            c+=1
            m = min(nums)
            while m == 0:
                nums.remove(0)
                m = min(nums)
            for i in range(len(nums)):
                nums[i] -= m
        return c
        
        