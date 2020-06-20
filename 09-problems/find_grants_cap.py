
# Analysis: Greedy
# 0. Initialization:
#    cap = new_budget / len(grants_array)
# 1. Greedy choice:
#    Choose the smallest budget, budget_i
#    If budget_i < cap, then the budget is kept, update new_budget (new_budget - budget_i ) and update cap (new_budget / # remaining budgets)
#    If budget_i >= cap, then the budget is cut, the remaining budget is updated
# 2. Prove that it's a safe choice:
# 3. Reduce to a smaller problem: remove current budget and iterate
# E.g. 2 50 100 120 1000; new_budget = 190
#      i   cap  new cap
#      0   38    47
#      1   47    47
#      ...  

# Time Analysis: O(|grantsArray| log |grantsArray|)
# Space Analysis: O(1)
def find_grants_cap(grants_array, new_budget):
    
    grants_array.sort()
    
    budget_count = len(grants_array)
    
    cap = new_budget / budget_count
    
    for i in range(budget_count):
        if grants_array[i] < cap:
            new_budget -= grants_array[i]
            cap = new_budget / (budget_count - i - 1)
        
        else:
            new_budget -= cap
            break
        
    return cap

