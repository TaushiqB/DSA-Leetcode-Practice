class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Specific Solution
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        five = 0
        ten = 0

        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five == 0:
                    return False
                else:
                    ten += 1
                    five -= 1
            else:
                if ten > 0 and 0 < five:
                    ten -= 1
                    five -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True
                
