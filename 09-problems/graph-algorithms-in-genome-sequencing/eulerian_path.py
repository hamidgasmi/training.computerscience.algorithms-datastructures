import sys
import eulerian_cycle

def eulerian_path(edges):

    graph = eulerian_cycle.Graph(edges)

    graph.find_unbalanced_vertices()

    path = []
    if len(graph.unbalanced_vertices) == 0:
        # The graph is balanced: let's try to find an Eurelian Cycle (it must be strongly connected)
        path = graph.eulerian_cycle()

    elif len(graph.unbalanced_vertices) == 2:
        u = graph.unbalanced_vertices[0].vertex_no
        u_in_degree = graph.unbalanced_vertices[0].in_degree
        u_out_degree = graph.unbalanced_vertices[0].out_degree

        v = graph.unbalanced_vertices[1].vertex_no
        v_in_degree = graph.unbalanced_vertices[1].in_degree
        v_out_degree = graph.unbalanced_vertices[1].out_degree
    
        if (u_in_degree - u_out_degree) * (v_in_degree - v_out_degree) == -1:
            # Add an additional edge
            if u_in_degree > u_out_degree:
                add_edge_start = u
                add_edge_end = v

            else:
                add_edge_start = v
                add_edge_end = u

            graph.adjacency_list[add_edge_start]. append(add_edge_end)
            
            # Find an Eulerian Cycle with the additional edge (it must be strongly connected)
            cycle = graph.eulerian_cycle()

            # Remove the additional edge from the cycle
            edge_position_in_cycle = -1
            for i in range(len(cycle) - 1):
                if cycle[i] == add_edge_start and cycle[i + 1] == add_edge_end:
                    edge_position_in_cycle = i
                    break

            assert(edge_position_in_cycle != -1)

            if edge_position_in_cycle == len(cycle) - 2:
                path = cycle [0: edge_position_in_cycle + 1]

            elif edge_position_in_cycle == 0:
                path = cycle [1: ]

            else:
                path = cycle [edge_position_in_cycle + 1: ]
                path.extend(cycle [1: edge_position_in_cycle + 1])

    return '->'.join( [ graph.nodes[node] for node in path ] )

if __name__ == "__main__":
    edges = sys.stdin.read().strip().splitlines()

    print(eulerian_path(edges))
