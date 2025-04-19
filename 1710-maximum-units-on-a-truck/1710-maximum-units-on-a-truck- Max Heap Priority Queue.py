class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Using Max Heap
        heap = [(-units, boxes) for boxes, units in boxTypes] # O(N) - Heap Space
        heapq.heapify(heap)   # O(N) - Heapify 

        ans = 0

        while heap and truckSize:    # O(N) - Loop
            units, boxes = heapq.heappop(heap) # O(log N) - Heappop
            
            if boxes <= truckSize:
                truckSize -= boxes
                ans += (boxes * units * -1)
            else:
                ans += (truckSize * units * -1)
                truckSize = 0
                
        return ans