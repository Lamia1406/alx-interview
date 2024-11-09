#!/usr/bin/python3
import sys
solution = []


def backtrack(queens, row=0):
    if row == int(queens):
        print(solution)
        return
    for j in range(int(queens)):
        candidate = [row, j]
        aligned = False
        for [m, n] in solution:
            if n == j:
                aligned = True
                break
            if abs(row - m) == abs(j - n):
                aligned = True
                break
        if not aligned:
            solution.append(candidate)
            backtrack(queens, row + 1)
            solution.pop()


if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


backtrack(sys.argv[1])
