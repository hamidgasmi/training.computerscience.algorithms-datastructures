#Uses python3
import os
import sys
import itertools

# Analysis:
# There're |V| vertices, let v be a vertice: 1 <= v <= 500
# There're 3 colors, let c be a color: 1 <= c <= 3
# Let Xvc be a literal that corresponds to a vertice v colored with c:
# A vertice must be colored only once: 
#     (Xv1 V Xv2 V Xv3)(-Xv1 V -Xv2)(-Xv1 V -Xv3)(-Xv2 v -Xv3)
# Let (u, w) 2 vertices adjacent to v: u, v, w must have different colors:
#     (Xv1 V Xu1 V Xw1)(-Xv1 V -Xu1)(-Xv1 V -Xw1)(-Xu1 V -Xw1)
#     (Xv2 V Xu2 V Xw2)(-Xv2 V -Xu2)(-Xv2 V -Xw2)(-Xu2 V -Xw2)
#     (Xv3 V Xu3 V Xw3)(-Xv3 V -Xu3)(-Xv3 V -Xw3)(-Xu3 V -Xw3)

clauses = []

colors = range(1, 4)

def vertice_color_num(v, color):
    assert(color in colors)
    return len(colors) * v + color

def exactly_one_of(literals):
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def createClauses(n, edges):

    adjacency_list = [[] for _ in range(n)]
    for (a, b) in edges:
        adjacency_list[a - 1].append(b - 1)
        adjacency_list[b - 1].append(a - 1)

    clauses_set = set()
    for v in range(n):

        # v must have 1 color only:
        exactly_one_of([vertice_color_num(v, color) for color in colors])

        for color in colors:
            literals = []
            literals.append(vertice_color_num(v, color))
            adjacency_colors_num = vertice_color_num(v, color)
            for a in adjacency_list[v]:
                adjacency_colors_num += vertice_color_num(a, color)
                literals.append(vertice_color_num(a, color))

            if adjacency_colors_num in clauses_set:
                continue
            exactly_one_of(literals)
            clauses_set.add(adjacency_colors_num)

def printEquisatisfiableSatFormula(n):
    
    print(len(clauses), n * 3)
    for c in clauses:
        for l in c:
            print(l, end=" ")
            
        print(0, end="")
        print("")

if __name__ == '__main__':
    
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]
    
    createClauses(n, edges)
    printEquisatisfiableSatFormula(n)

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
