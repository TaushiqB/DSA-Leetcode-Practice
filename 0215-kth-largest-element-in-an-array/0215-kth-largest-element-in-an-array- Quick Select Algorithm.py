class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Using Quick Select Algorithm
        # We partition the list into two based on the pivot
        # And put the smaller than pivot elements towards left of it and larger than elements towards left of it
        # Use Recursion to find the answer
        # Average case: O(n) Worst Case: O(n^2)
        k = len(nums) - k  # Target Index
        def quickselect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            nums[r], nums[p] = nums[p], nums[r]
            # K is within l and P
            if p > k: 
                quickselect(l, p-1)
            # K is within p and R
            if p < k:
                quickselect(p+1, r)
            else:
                return nums[p]
        quickselect(0, len(nums)-1)
        return nums[k]
