class DisjointSet:

    def __init__(self, nodes_count: int):     
        self.rank = [0 for _ in range(nodes_count)]
        self.parent = [i for i in range(nodes_count)]
    
    def find(self, i):
        # 1. find parent
        root = i
        while self.parent[root] != root:
            root = self.parent[root]
        
        # 2. Compress Path
        while i != root:
            self.parent[i], i = root, self.parent[i]
        
        return root
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i == root_j:
            return
        
        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
            
        else:
            self.parent[root_i] = root_j
            
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_j] += 1

class SolutionUnionFind:

    def largest_component_size(self, A: List[int]) -> int:
                
        # 1. Compute Factors & Compute Common Disjoint Sets
        disjoint_set = DisjointSet(max(A) + 1)
        for n in A:
            factors = self.get_prime_factors(n)
            
            disjoint_set.union(n, factors[0])
        
            for i in range(1, len(factors)):
                disjoint_set.union(factors[i-1], factors[i])
        
        # 3. Find the largest component size
        max_size = 0
        components_size = dict()
        for i in range(len(A)):
            root = disjoint_set.find(A[i])
            components_size[root] = components_size.get(root, 0) + 1
            
            max_size = max(max_size, components_size[root])
        
        return max_size
    
    def get_prime_factors(self, n):
        
        factor = 2
        prime_factors = []
        while n >= factor * factor:
            if n % factor == 0:
                prime_factors.append(factor)
                n //= factor
            else:
                factor += 1
        prime_factors.append(n)
        
        return prime_factors

class SolutionDFS:
    
    def largest_component_size(self, A: List[int]) -> int:
        
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