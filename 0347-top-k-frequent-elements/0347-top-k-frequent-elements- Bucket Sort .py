class Solution(object):
    def topKFrequent(self, nums, k):
        # Bucket Sort
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1

        bucket = [[] for i in range(len(nums)+1)]
        for key, val in h.items():
            bucket[val].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res