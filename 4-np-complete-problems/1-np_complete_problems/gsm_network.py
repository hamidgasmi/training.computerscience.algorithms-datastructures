import os
import sys
import itertools

# Analysis:
# There're |V| vertices, let v be a vertice: 1 <= v <= 500
# There're 3 colors, let c be a color: 1 <= c <= 3
# Let Xvc be a literal that corresponds to a vertice v colored with c:
#     E.g., for v = 1
#           X11 = 3 * 0 + 1 = 1
#           X12 = 2
#           X13 = 3
#     E.g., for v = 2
#           X11 = 3 * (2 - 1) + 1 = 4
#           X12 = 5
#           X13 = 6
# A vertice must be colored:
#     (Xv1 V Xv2 V Xv3)
# A vertice can't have 2 different colors at the same time: it must be colored only once: 
#     (-Xv1 V -Xv2)(-Xv1 V -Xv3)(-Xv2 v -Xv3)
# Vertice (u, w) adjacents to v must have different colors:
#     (Xv1 V Xu1 V Xw1)(-Xv1 V -Xu1)(-Xv1 V -Xw1)(-Xu1 V -Xw1)
#     (Xv2 V Xu2 V Xw2)(-Xv2 V -Xu2)(-Xv2 V -Xw2)(-Xu2 V -Xw2)
#     (Xv3 V Xu3 V Xw3)(-Xv3 V -Xu3)(-Xv3 V -Xw3)(-Xu3 V -Xw3)
clauses = []

colors = range(1, 4)

def vertice_color_num(v, color):
    assert(color in colors)
    return len(colors) * (v - 1) + color

def exactly_one_of(literals):
    if len(literals) >= len(colors):
        clauses.append([l for l in literals])

    not_same_value(literals)

def not_same_value(literals):
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def create_sat_clauses(n, edges):

    adjacency_list = [[] for _ in range(n)]
    for (a, b) in edges:
        adjacency_list[a - 1].append(b)
        adjacency_list[b - 1].append(a)

    clauses_set = set()
    for i in range(n):

        v = i + 1

        # Clause 1: vertice v has exactly color:
        exactly_one_of([vertice_color_num(v, color) for color in colors])

        if len(adjacency_list[i]) == 0:
            continue
        
        # Clause 2: 2 adjacent vertices must have different colors
        # Clauses corresponding to an edge A --- B must be generated only once
        for a in adjacency_list[i]:
            edge_num = max(a, v) * 1000 + min(a, v)

            if edge_num in clauses_set:
                continue
            
            clauses_set.add(edge_num)

            for color in colors:
                literals = []
                literals.append(vertice_color_num(v, color))
                literals.append(vertice_color_num(a, color))
                not_same_value(literals)

def print_equisatisfiable_sat_formula(n):
    
    print(len(clauses), n * 3)
    for c in clauses:
        for l in c:
            print(l, end=" ")
        print(0, end="")
        print("")

def sat_solver():
    with open('tmp.cnf', 'w') as f:
        f.write("p cnf {} {}\n".format(n * 3, len(clauses)))
        for c in clauses:
            c.append(0)
            f.write(" ".join(map(str, c))+"\n")

    os.system("minisat tmp.cnf tmp.sat")

    with open("tmp.sat", "r") as satfile:
        for line in satfile:
            if line.split()[0] == "UNSAT":
                print("There is no solution")

            elif line.split()[0] == "SAT":
                print("SATISFIABLE")

    os.remove("tmp.sat")
    os.remove("tmp.cnf")

if __name__ == '__main__':
    
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]
    
    create_sat_clauses(n, edges)
    print_equisatisfiable_sat_formula(n)
    sat_solver()
