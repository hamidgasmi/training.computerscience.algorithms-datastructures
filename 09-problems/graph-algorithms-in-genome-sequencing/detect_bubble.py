import sys
from queue import Queue

class De_Bruijn_Graph:
    def __init__(self, k, t, reads):
        
        assert(k > 1)
        assert(len(reads[0]) >= k)

        self._bubble_treshold = t

        self._build_gragh(k, reads)

    def _build_gragh(self, k, reads):
        
        self.nodes = []
        self.adjacency_list = []
        self.in_degree = []
        self.out_degree = [] 

        node_kmer_no_dict = dict()
        for read in reads:
            for i in range(len(read) - k + 1):

                prefix_node_no = self._get_node_no(read[0:k-1], node_kmer_no_dict) if i == 0 else suffix_node_no
                suffix_node_no = self._get_node_no(read[i+1:i+k], node_kmer_no_dict)
                
                if suffix_node_no in self.adjacency_list[prefix_node_no]:
                    continue

                self.adjacency_list[prefix_node_no].add(suffix_node_no)

                if prefix_node_no == suffix_node_no:
                    continue
                
                self.out_degree[prefix_node_no] += 1
                self.in_degree[suffix_node_no] += 1
            
    def _get_node_no(self, label, node_label_no_dict):
        
        if label in node_label_no_dict:
            node_no = node_label_no_dict[label]

        else:
            node_no = len(self.nodes)
            self.nodes.append(label)
            self.adjacency_list.append(set())
            self.in_degree.append(0)
            self.out_degree.append(0)
            node_label_no_dict[label] = node_no

        return node_no
    
    def short_paths_bfs(self, u, short_paths, bubble_treshold):
        
        # path as an array: to get path last element in O(1) time
        q_paths = Queue()
        # path as a set(): to check if a node is in the path in O(1)
        q_paths_set = Queue()

        q_paths.put([u])
        q_paths_set.put({u})

        while not q_paths.empty():
            
            path = q_paths.get()
            path_set = q_paths_set.get()

            path_tail_node = path[len(path) - 1]

            if (path_tail_node != u) and (not path_tail_node in short_paths):
                    short_paths[ path_tail_node ] = []
            
            if len(path) > 1:
                short_paths[ path_tail_node ].append(path_set.copy())
                short_paths[ path_tail_node ][ len(short_paths[ path_tail_node ]) - 1 ].remove(path[0])
                short_paths[ path_tail_node ][ len(short_paths[ path_tail_node ]) - 1 ].remove(path_tail_node)

            if (len(path) - 1) >= bubble_treshold:
                continue
            
            for v in self.adjacency_list[path_tail_node]:
                
                if v in path_set:
                    continue
                
                # There is only 1 path going to a node which in_degree = out_degree = 1
                # It's not necessary to enqueue them
                w = v
                node_path = []
                node_path_set = set()
                while self.in_degree[w] == self.out_degree[w] == 1:
                    node_path.append(w)
                    node_path_set.add(w)

                    w = next(iter(self.adjacency_list[w]))
                    
                    if (len(path) + len(node_path) -1) >= bubble_treshold:
                        break
                node_path.append(w)
                node_path_set.add(w)
                
                # void cycles
                if w in path_set:
                    continue
                
                # dead-end node: there is only 1 path passing by
                if self.out_degree[w] == 0 and self.in_degree[w] == 1:
                    continue
                
                # Long path
                if (len(path) + len(node_path) - 1) > bubble_treshold:
                    continue
                
                q_paths_set.put(path_set.union(node_path_set))
                q_paths.put(path + node_path)
                
    def detect_bubbles(self):
                
        bubble_count = 0
        for u in range(len(self.nodes)):
            
            if self.out_degree[u] > 1:
                
                # short_paths contains all paths starting from u
                #    dict key = end path node (v)
                #    dict value: a list of all short paths from u to v (dict key)
                #              : u and v aren't included in path list
                #              : Each path is a set of nodes
                short_paths = dict()
                self.short_paths_bfs(u, short_paths, self._bubble_treshold)
                
                for paths in short_paths.values():
                    for i in range(len(paths)):
                        for j in range(i + 1, len(paths)):
                            bubble_count += 1 if paths[i].isdisjoint(paths[j]) else 0

        return bubble_count

if __name__ == "__main__":

    k, t = map(int, sys.stdin.readline().strip().split(" "))
    
    reads = sys.stdin.read().strip().splitlines()
    
    de_bruijn_graph = De_Bruijn_Graph(k, t, reads)
    
    print(de_bruijn_graph.detect_bubbles())