class SolutionDisjointSets:

class SolutionDFS:
    def largestComponentSize(self, A: List[int]) -> int:
        
        self.vertices_count = len(A)
        
        adjacency_list = self.build_graph(A)
        
        return self.dfs(adjacency_list)
    
    def build_graph(self, A: List[int]) -> List[List[int]]:
        
        factors = dict()
        
        for n in A:
            if n not in factors:
                factors[n] = set()
            self.get_factors(n, factors[n])
            
        adjacency_list = [[] for _ in range(self.vertices_count)]
        for i in range(self.vertices_count):
            n = A[i]
            for j in range(i + 1, self.vertices_count):
                m = A[j]
                if len(factors[n].intersection(factors[m])):
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)
        
        return adjacency_list
    
    def get_factors(self, n, factors_set):
                
        factor = 2
        while n >= factor * factor:
            if n % factor == 0:
                factors_set.add(factor)
                n //= factor
            else:
                factor += 1
        factors_set.add(n)
        
    def dfs(self, adjacency_list: List[List[int]]) -> int:
                
        visited = [False for _ in range(self.vertices_count)]
        
        largest_component_size = 0
        for u in range(self.vertices_count):
            if not visited[u]:
                largest_component_size = max(largest_component_size, self.explore(u, adjacency_list, visited))
        
        return largest_component_size
    
    def explore(self, u, adjacency_list, visited):
        if visited[u]:
            return 0
        
        size = 1
        visited[u] = True
        for v in adjacency_list[u]:
            if not visited[v]:
                size += self.explore(v, adjacency_list, visited)
        
        return size