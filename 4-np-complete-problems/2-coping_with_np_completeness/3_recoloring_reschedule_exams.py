# python3
import sat2_circuit_design

# Arguments:
#   * `n` - the number of vertices.
#   * `edges` - list of edges, each edge is a tuple (u, v), 1 <= u, v <= n.
#   * `colors` - list consisting of `n` characters, each belonging to the set {'R', 'G', 'B'}.
# Return value: 
#   * If there exists a proper recoloring, return value is a list containing new colors, similar to the `colors` argument.
#   * Otherwise, return value is None.
class Reduct_3_coloring_to_2_sat:

    def __init__(self, n, edges, colors):
        
        self.f_convert_3_coloring_imputs_to_2_sat(n, edges, colors)
        self.implication_graph = sat2_circuit_design.Implication_graph(n * 3, self.clauses)

    def color_num(self, color):
        
        return 1 if color == 'R' else 2 if color == 'G' else 3

    def sat_v_num(self, v_no, color):

        return 3 * (v_no - 1) + self.color_num(color)

    def f_convert_3_coloring_imputs_to_2_sat(self, n, edges, colors):
        self.clauses = []
        
        # Clauses 1: vertices possible colors
        # Clauses 2: a vertice can't have 2 different colors at the same time 
        # Clauses 2: vertices color must be changed
        for i in range(n):
            possible_colors_clause = []
            exactly_one_clause = []
            for c in range(3):
                if colors[0][i] == "RGB"[c % 3]:
                    self.clauses.append([- self.sat_v_num(i+1, colors[0][i])])
                else:
                    X = self.sat_v_num(i+1, "RGB"[c % 3])
                    possible_colors_clause.append(X)
                    exactly_one_clause.append(-X)
            
            self.clauses.append(possible_colors_clause)
            self.clauses.append(exactly_one_clause)
        
        # Clauses 2: Each vertice color must be different to all adjacent vertices color
        for (u, v) in edges:
            
            for c in range(3):
                adjacent_vertices_clauses = []
                adjacent_vertices_clauses.append(- self.sat_v_num(u, "RGB"[c % 3]))
                adjacent_vertices_clauses.append(- self.sat_v_num(v, "RGB"[c % 3]))
                self.clauses.append(adjacent_vertices_clauses)

    def solve_2_sat(self):
        self.sat_solution = self.implication_graph.solve_2sat(True)

    def h_convert_2_sat_output_to_3_coloring(self):
        
        if self.sat_solution == None:
            return None

        new_colors = []
        #print(self.clauses)
        #print(self.sat_solution)
        for i in range(len(self.sat_solution)):
            if self.sat_solution[i] == 1:
                new_colors.append("RBG"[(i)% 3])

        return new_colors
 
def assign_new_colors(n, edges, colors):

    reduction_to_2_sat = Reduct_3_coloring_to_2_sat(n, edges, colors)
    reduction_to_2_sat.solve_2_sat()
    return reduction_to_2_sat.h_convert_2_sat_output_to_3_coloring()
    
def main():
    n, m = map(int, input().split())
    colors = input().split()
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    new_colors = assign_new_colors(n, edges, colors)
    if new_colors is None:
        print("Impossible")
    else:
        print(''.join(new_colors))

if __name__ == "__main__":
    main()
