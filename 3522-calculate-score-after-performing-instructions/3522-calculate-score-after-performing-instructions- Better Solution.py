"""
        Calculates the score by following the instructions in order.
        Each instruction is one of:
        - "add": Add the corresponding value to the score and move to the next instruction.
        - "jump": Move to the next instruction by jumping `values[i]` steps.
        - "exit": Stop execution.

        An instruction is executed at most once. Execution stops if the current index goes out of bounds
        or the instruction has already been visited.

        Time Complexity: O(n) — Each instruction is visited at most once.
        Space Complexity: O(1) — Constant extra space (modifying input in-place).
"""

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:

        n = len(instructions)
        s = 0
        i = 0
        while 0 <= i < n:
            print(i)
            inst, instructions[i] = instructions[i], "Visited"
            if inst == "add":
                s+=values[i]
                i+=1
            elif inst == "jump":
                i+=values[i]
            else:
                break
        return s