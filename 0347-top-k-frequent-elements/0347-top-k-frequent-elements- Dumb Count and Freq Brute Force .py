class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Counting and Freq Approach
        max_val = max(nums)
        min_val = min(nums)
        ans = [0]*(max_val - min_val + 1)

        for i in nums:
            ans[i - min_val] += 1
        a = []
        while k:
            m = max(ans)
            for i in range(len(ans)):
                if m == ans[i]:
                    a.append(i+min_val)
                    ans[i] = -1
                    k -= 1

        return a
            
        
        