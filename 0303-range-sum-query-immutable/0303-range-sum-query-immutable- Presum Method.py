class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = nums
        for i in range(len(nums)-1):
            self.presum[i+1] += self.presum[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.presum[right]
        return self.presum[right] - self.presum[left-1]

# Your NumArray object will be instantiated and called as such:
#obj = NumArray(nums)
#param_1 = obj.sumRange(left,right)
