import sys


def eulerian_cycle(graph):
    """Finds an Eulerian cycle in the given graph

    Args:
        graph:      a list of strings containing edges in the graph; one
                    string may correspond to multiple edges if it is of the
                    form "X -> Y,Z"

    Returns:
        a string containing an Eulerian cycle through the given graph
    """
    # TODO: your code here
    return ""


if __name__ == "__main__":
    graph = sys.stdin.read().strip().splitlines()
    print(eulerian_cycle(graph))
