import sys

class De_Bruijn_Graph:
    def __init__(self, k, text):
        pass

    def _build_adjacency_list(self):
        pass

    def str_adjacency_list(self):
        pass

if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())
    text = sys.stdin.readline().strip()

    de_bruijn_graph = De_Bruijn_Graph(k, text)
    
    print(de_bruijn_graph.str_adjacency_list())