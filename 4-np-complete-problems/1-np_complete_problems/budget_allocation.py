# python3
import itertools
from sys import stdin

# Analysis:
# Let Xi a boolean variable for i in { 1, 2, 3 }
# For each inequality, find all vectors X (X1, X2, X3) that invalidate the inequality:
# ... There're 8 different vectors X
# ... Add a clause for each invalidating vector
# ... If 0 0 0 is invalidating the inequality, (X1, X2, X3) shound't be equal to (0, 0, 0)
# ... It's equivalent to: X1 V X2 V X3
def build_clauses(A, b, clauses):

    unsatisfiable = False  
    var_nbr = len(A[0])
    # Clause: Xi Values that are invalidating an inequality must be excluded
    combination_nbr = 2 ** var_nbr
    for combination in itertools.product(range(2), repeat=var_nbr):

      clause = []
      for i in range(var_nbr):
        clause.append(i+1 if combination[i] == 0 else -i-1)

      for i in range(len(b)):

        a = A[i]

        unsatisfiable = True if b[i] < 0 else False
        inequality_left_part = 0
        for j in range(var_nbr):
          inequality_left_part += a[j] * combination[j]
          unsatisfiable = unsatisfiable if a[j] == 0 else False
          
        if unsatisfiable:
          break
        
        if inequality_left_part > b[i]:
          clauses.append(clause)
          break
      
      if len(clauses) == combination_nbr:
        unsatisfiable = True

      if unsatisfiable:
        break
    
    if unsatisfiable:
      clauses.clear()
      clauses.append([1])
      clauses.append([-1])
      var_nbr = 1
      
    elif len(clauses) == 0:
      clauses.append([1, -1])
      var_nbr = 1
    
    return var_nbr

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
  var_nbr = build_clauses(A, b, clauses)

  printEquisatisfiableSatFormula(clauses, var_nbr)
