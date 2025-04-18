class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # Prefix Sum and Hash Map Almost Brute Force
        candlesl = [-1]*len(s) # To have candles left
        candlesr = [len(s)]*len(s) # To have Candles right
        counter = 0
        candles = {}
        lastcandle = -1
        # To input into left candles:
        for i in range(len(s)):
            if s[i] == '|':
                candles[i] = counter
                counter+=1
                lastcandle = i
            candlesl[i] = lastcandle

        # To input into right candles:
        for i in range(len(s)-1, -1, -1):
            if s[i] == '|':
                lastcandle = i
            candlesr[i] = lastcandle           

        print(candlesr)
        print(candlesl)
        print(candles)
        # Go through Query
        # Figure out the numbers of candles between the right and left
        # Right most candle - left most candle - 1 - number of candles between them.
        ans = []
        for i in queries:
            leftq, rightq = i[0], i[1]
            plates = candlesl[rightq] - candlesr[leftq] - 1
            plates -= candles.get(candlesl[rightq],0) - candles.get(candlesr[leftq],0) - 1
            ans.append(max(plates, 0))
        return ans
            