import sys
import math

# 1. Express a solution mathematically: 
#    We know: Pr(x | P ) = Product(i=1..n, Pr(xi|Pi)) = Product(i=1..n, emission(Pi, xi))
#             Pr(P) = Product(i=1..n, Pr(Pi-1 --> Pi)) = Product(i=1..n, transition(Pi-1, Pi))
#           Then Pr(P, x) = Pr(x | P ) * Pr(P) = Product(i=1..n, emission(Pi, xi)) * Product(i=1..n, transition(Pi-1, Pi))
#           So, Pr(optimal P, x) = Max Pr(x | P ) * Pr(P) = Product(i=1..n, emission(Pi, xi)) * Product(i=1..n, transition(Pi-1, Pi))
# 2. Proof: 
# 3. Solutions: we can solve this problem wit a DP technique + Bottom up solution:
#    1. We build the corresponding graph matrix (|states| . |x|)
#       - M[state_i,p] = max(M[state_j, p - 1] * transition[state_j][state_i] * emission[state_i][xp]
#       - To avoid the risk of stackoverflow error, we'll use logarithm:
#       - log(M[state_i,p]) = max(M[state_j, p - 1] + log(transition[state_j][state_i]) + log(emission[state_i][xp]))
#    2. From the matrix, M, we'll use the backtracking approach to build the hidden path
def build_optimal_path_backtrack(x, states, transition, emission, M):
    
    optimal_hidden_path = ['' for _ in range(len(x))]

    opt_state = util_column_max_value_index(M, len(states), len(x) - 1)
    optimal_hidden_path[len(x) - 1] = states[opt_state]
    for p in range(len(x) - 1, 0, -1):
        curr_x = x[p]
        
        for s in range(len(states)):
            if M[opt_state][p] == M[s][p - 1] + util_sum_log_vals((transition[ states[s] ][ states[opt_state] ], emission[ states[opt_state] ][ curr_x ])):
                  opt_state = s
                  break
        optimal_hidden_path[p - 1] = states[opt_state]
    
    return optimal_hidden_path

def optimal_path(x, sigma, states, transition, emission):
    
    # The transitions from the initial state occur with equal probability: Prob(P0 = Si) = 1/|states| * Pr(x = x0 | P0)
    M = [ [util_sum_log_vals((1/len(states), emission[ states[s] ][ x[0] ])) if p == 0 else 0 for p in range(len(x))] for s in range(len(states)) ]
        
    for p in range(len(x) - 1):
        next_x = x[p + 1]

        for s in range(len(states)):
            M[s][p + 1] = -math.inf if M[0][p] == -math.inf else M[0][p] + util_sum_log_vals((transition[ states[0] ][ states[s] ], emission[ states[s] ][ next_x ]))

        for s in range(1, len(states)):
            for next_s in range(len(states)):
                if M[s][p] == - math.inf:
                    continue
                
                candidate_probability = M[s][p] +  util_sum_log_vals((transition[ states[s] ][ states[next_s] ], emission[ states[next_s] ][ next_x ]))
                if candidate_probability > M[next_s][p + 1]:
                    M[next_s][p + 1] = candidate_probability
    
    optimal_hidden_path = build_optimal_path_backtrack(x, states, transition, emission, M)
    
    return ''.join(optimal_hidden_path)

def util_sum_log_vals(vals):
    sum_log = 0
    for val in vals:
        assert(val >= 0)
        if val == 0:
            sum_log = - math.inf
            break
        else:
            sum_log += math.log(val)

    return sum_log

def util_column_max_value_index(matrix, rows_count, c):
    assert(rows_count > 0)
    assert(c < len(matrix[0]))

    row_max_value = 0
    for r in range(1, rows_count):
        if matrix[r][c] > matrix[row_max_value][c]:
            row_max_value = r

    return row_max_value

if __name__ == "__main__":
    x = sys.stdin.readline().strip()
    sys.stdin.readline() # delimiter

    sigma = sys.stdin.readline().strip().split()
    sys.stdin.readline() # delimiter

    states = sys.stdin.readline().strip().split()
    sys.stdin.readline() # delimiter

    chars = sys.stdin.readline().strip().split() 
    transition = [sys.stdin.readline().strip().split() for _ in range(len(states))]
    transition = {line[0]:dict(zip(chars, map(float,line[1:]))) for line in transition}
    sys.stdin.readline() # delimiter

    chars = sys.stdin.readline().strip().split() 
    emission = [sys.stdin.readline().strip().split() for _ in range(len(states))]
    emission = {line[0]:dict(zip(chars, map(float,line[1:]))) for line in emission}
    
    print(optimal_path(x,sigma,states,transition,emission))
