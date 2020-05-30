#Uses python3
import itertools
from sys import stdin

# Analysis:
# Let Xi a boolean variable for i in { 1, 2, 3, ..., n }
# For each inequality, find all vectors X (Xi, Xj, Xk) that invalidate the inequality:
# ... Add a clause for each invalidating vector
# ... If 0 0 0 is invalidating the inequality, (X1, X2, X3) shound't be equal to (0, 0, 0)
# ... It's equivalent to: X1 V X2 V X3
# Special Cases:
# ... If all coefficient are equal to 0 for an inequality and b < 0, then there is no solution
# ... If the formula reaches 8 cases, then there is no solution
def build_clauses(A, b, formula):
  
    # Clause: Xi Values that are invalidating an inequality must be excluded
    unsatisfiable = False
    var_nbr = 0
    var_no_map = [0] * len(A[0])
    for i in range(len(b)):

        a = []
        ineq_var = []
        for j in range(len(A[i])):
          if A[i][j] == 0:
            continue
          
          a.append(A[i][j])
          # Find the variable No
          if var_no_map[j] == 0:
            var_nbr += 1
            var_no_map[j] = var_nbr
          ineq_var.append(var_no_map[j])
          
        ineq_var_nbr = len(a) # <= 3

        unsatisfiable = False
        if ineq_var_nbr == 0 and b[i] < 0:
          unsatisfiable = True
          break
        elif ineq_var_nbr == 0:
          continue

        for combination in itertools.product(range(2), repeat=ineq_var_nbr):
          
          clause = []
          inequality_left_part = 0
          for j in range(ineq_var_nbr):
            inequality_left_part += a[j] * combination[j]
            clause.append(ineq_var[j] if combination[j] == 0 else -ineq_var[j])
          
          if inequality_left_part > b[i]:
            formula.append(clause)

    if len(formula) >= 2**var_nbr:
      unsatisfiable = True

    if unsatisfiable:
      formula.clear()
      formula.append([1])
      formula.append([-1])
      var_nbr = 1
      
    elif len(formula) == 0:
      formula.append([1, -1])
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
