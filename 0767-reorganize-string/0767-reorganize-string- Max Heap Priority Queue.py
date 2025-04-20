class Solution:
    def reorganizeString(self, s: str) -> str:
        # Priority Queue Using a Max Heap
        # While heap has more than two characters, pop the highest character and the second highest
        # if the characters are exjausted and one character remains and its count is greater than one
        # Then no matter how arrange it, its not ginna work.
        # Even if it is one check that it is not the last character we included.

        # Time Complexity  - O(nlogk)
        # Space Complesity - O(n)
        f = {}
        if len(s) == 1:
            return s
        for c in s:  # O(n) To traverse through the string to calculate the ferquency
            f[c] = f.get(c, 0) + 1

        heap = [(-count, char) for char, count in f.items()]      # O(n)
        heapq.heapify(heap)                                       # Heapify takes O(klogk) times

        res = []
        while len(heap) >= 2:
            top_count, top_char = heapq.heappop(heap)
            next_count, next_char = heapq.heappop(heap)
            res.append(top_char)
            res.append(next_char)
            if top_count+1:
                heapq.heappush(heap, (top_count+1, top_char))
            if next_count+1:            
                heapq.heappush(heap, (next_count+1, next_char))
        if heap:
            top_count, top_char = heapq.heappop(heap)
            if top_count != -1 or top_char == res[-1]:
                return ''
            else:
                res.append(top_char)
        return "".join(res)