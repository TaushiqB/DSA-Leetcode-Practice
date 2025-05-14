class Solution:
    def checkValidString(self, s: str) -> bool:
        # Striver Range Method Similar to the Count Method
        Min = 0
        Max = 0
        for i in range(len(s)):
            if s[i] == '(':
                Min+=1
                Max+=1
            elif s[i] == ')':
                Min-=1
                Max-=1
            elif s[i] == '*':
                Min-=1
                Max+=1
            if Min < 0:
                Min = 0          # When it goes less than zero, its unwanted.
            if Max < 0:
                return False     # The Moment Max Goes below 0, its False
        if Min == 0:
            return True
        return False