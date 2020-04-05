# python3
from sys import stdin

# Analysis:
# For each inequality:
# For each variable in the inequality, find all possible validating values
# Build clauses that are related to variable possible values:
# ... Let be Xiv a boolean literal that is true if the variable i is equal to a value v
# ... 1- A variable must be assigned a value: (Xiv1 V Xiv2 + ... Xivn)
# ... 2- A variable must be assigned a value only once: (-Xiv1 V Xiv2) for all v1 != v2
# Build clauses that are related to variable values that are invalidating the inequality:
# ... Let be X: (X1v1, X2v2, ..., Xnvn) a vector of k variables created from possible validating variable values Xiv above
# ... 3- Variables Xiv that form a vector X that is invalidating the inequality must be excluded: (-X1v1 V -X2V2 V ... V -XkVk)


# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    print("1 1")
    print("1 -1 0")

if __name__ == "__main__":

  n, m = list(map(int, stdin.readline().split()))
  A = []
  for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
  b = list(map(int, stdin.readline().split()))

  printEquisatisfiableSatFormula()
