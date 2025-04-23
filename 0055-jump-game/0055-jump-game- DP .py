class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #dynamic Programming Shit
        @cache
        def jump(i):
            if i >= len(nums)-1:
                return True
            elif nums[i] == 0:
                return False
            else:
                for k in range(nums[i], 0, -1):
                    if jump(i+k):
                        return True
                return False

        return jump(0)
            