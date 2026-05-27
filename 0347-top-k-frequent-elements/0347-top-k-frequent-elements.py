from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = Counter(nums)

        heap = []

        for num, count in freq.items():
            heapq.heappush(heap,(-count, num))

        res = []

        for _ in range(k):
            count, num = heapq.heappop(heap)
            res.append(num)

        return res
