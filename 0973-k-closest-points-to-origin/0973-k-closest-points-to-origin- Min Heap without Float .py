
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min Heap and Priority Queue
        heap = []
        res = []  
        for i in points:
            dist = i[0]**2 + i[1]**2
            heapq.heappush(heap, (dist, i)) # heapify the distance and the points
        print(heap)
        for i in range(k):
            res.append(list(heapq.heappop(heap)[1])) # Append only the points
        return res # Return the list of points
