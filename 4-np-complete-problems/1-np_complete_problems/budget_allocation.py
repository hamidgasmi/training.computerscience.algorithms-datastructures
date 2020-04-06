# python3
import itertools
from sys import stdin


# Analysis:
# Let Xi a boolean variable for i in { 1, 2, 3 }:
# Each variable Xi must have a value: (Xi V -Xi)
# For each inequality, find all  vectors X (X1, X2, X3) that invalidate the inequality:
# ... There're 8 different vectors X
# ... Add a clause for each invalidating vector

def add_inequality_invalidating_clauses(a, b, clauses):
  
  len_a = len(a)
  for combination in itertools.product(range(2), repeat=len_a):
    inequality_left_part = a[0] * combination[0]
    inequality_left_part += a[1] * combination[1] if len_a > 1 else 0
    inequality_left_part += a[2] * combination[2] if len_a == 3 else 0
    
    if inequality_left_part > b:
      clauses.append([1 if combination[0] == 0 else -1])
      if len_a > 1:
        clauses[len(clauses) - 1].append(2 if combination[1] == 0 else -2)
      if len_a == 3:
        clauses[len(clauses) - 1].append(3 if combination[2] == 0 else -3)
      
     
def build_clauses(A, b, clauses):

    # Adding clauses corresponding to possible values for Xi: Xi V -Xi
    clauses.append([-1, 1]) # X1
    var_nbr = 1
    for a in A:
      if len(a) > 1 and len(clauses) == 1:
        clauses.append([-2, 2]) # X2
        var_nbr += 1
      if len(a) == 3 and len(clauses) == 2:
        clauses.append([-3, 3]) # X3
        var_nbr += 1

      if var_nbr == 3:
        break
    
    # Adding Clauses corresponding to values that invalidate each inequality
    for i in range(len(b)):
      add_inequality_invalidating_clauses(A[i], b[i], clauses)

    return var_nbr
  
def printEquisatisfiableSatFormula(clauses, var_nbr):

  print(len(clauses), var_nbr)
  for c in clauses:
    for l in c:
      print(l, end=" ")
    print(0, end="")
    print("")
  
if __name__ == "__main__":

  n, m = list(map(int, stdin.readline().split()))
  A = []
  for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
  b = list(map(int, stdin.readline().split()))

  clauses = []
  var_nbr = build_clauses(A, b, clauses)

  printEquisatisfiableSatFormula(clauses, var_nbr)
