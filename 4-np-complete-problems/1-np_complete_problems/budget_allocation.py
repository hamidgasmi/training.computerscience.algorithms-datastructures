# python3
import itertools
from sys import stdin


# Analysis:
# Let Xi a boolean variable for i in { 1, 2, 3 }:
# Each variable Xi must have a value: (Xi V -Xi)
# For each inequality, find all vectors X (X1, X2, X3) that invalidate the inequality:
# ... There're 8 different vectors X
# ... Add a clause for each invalidating vector
def add_inequality_invalidating_clauses(a, b, clauses):
  
  len_a = len(a)
  for combination in itertools.product(range(2), repeat=len_a):
    
    inequality_left_part = 0
    for i in range(len_a):
      inequality_left_part += a[i] * combination[i]

    if inequality_left_part > b:
      clauses.append([])
      for i in range(len_a):
        clauses[len(clauses) - 1].append(i+1 if combination[i] == 0 else -i-1)
      if (len(clauses) == 2):
        print("a: ", a)
        print("combination: ", combination)
        print("clauses[1]", clauses[1])

def build_clauses(A, b, clauses):

    # 1. Adding clauses corresponding to possible values for Xi: Xi V -Xi
    clauses.append([])
    for Xi in range(1, len(A[0]) + 1):
        clauses[0].append(Xi)
        clauses.append([-Xi, Xi])
    
    # 2. Adding Clauses corresponding to values that invalidate each inequality
    for i in range(len(b)):
      add_inequality_invalidating_clauses(A[i], b[i], clauses)
  
def printEquisatisfiableSatFormula(clauses, var_nbr):

  print(len(clauses), var_nbr)
  for c in clauses:
    for l in c:
      print(l, end=" ")
    print(0, end="")
    print("")
  
if __name__ == "__main__":

  ineq_nbr, var_nbr = list(map(int, stdin.readline().split()))
  A = []
  for i in range(ineq_nbr):
    A += [list(map(int, stdin.readline().split()))]
  b = list(map(int, stdin.readline().split()))

  clauses = []
  build_clauses(A, b, clauses)

  printEquisatisfiableSatFormula(clauses, var_nbr)
