class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        # Brute Force solution
        s = 0 # Create a variable to store score
        ind = [False]*len(values) # Create a list to mark traversed indexes as True
        i = 0
        while 0 <= i < len(values) and not(ind[i]):
            print(i)
            ind[i] = True
            if instructions[i] == "add":
                s += values[i]
                i+=1
            else:
                i+=values[i]
        return s

        # Time Complexity: O(n) - One loop
        # Space Complexity: O(n) - for ind array