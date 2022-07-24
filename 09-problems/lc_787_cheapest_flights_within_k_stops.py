"""
    1. Problem Summary / Clarifications / TDD:
        Directed Graph(V: { Cities }, E: { Flights }, W: { Prices } )
        K: Number max stops
        Question: Return price of cheapest flight from city "SRC" to city "DST" with at most K stops

        With Graph below, SRC: C0, DST: C2
        Expected Results: 

           2           1
       C3 ___   C2 <----- 
        ^    \   ^       |
      2 |     \  | 5      --C4
       C0 ---_> C1-----------^
            5          1
                                                  5       1       1
        Expected result for K = 3: 7 (3 Stops: C0 ---> C1 ---> C4 ---> C2)

                                                  2      2       1       1
        Expected result for K = 4: 6 (4 Stops: C0 --> C3 ---> C1 ---> C4 ---> C2)

    2. Intuition:
        - Kind of BFS + Optimizations: O(|V|^2 + |V||E|) ?
            - to have a variable dst cheapest path price (initialized to Infinity)
            - To visit cities multiple-times: when curr visit path price < prev visit path price
            - To stop a path if its price > dst cheapest path price
        - DFS + memoization:
        - Dijkstra:

    3. Implementation
    4. Tests:
    5. Complexity Analysis:
       Time Complexity:
       Space Compexity:

"""
import heapq
from typing import List

class Solution_Base:
    def __init__(self):
        self.__max_pirce = 10**8

    """
        Time Complexity: O(|E|)
        Space Complexity: O(|V| + |E|)
    """
    def __build_adjacency_list(self, cities_count: int, edges: List[List[int]]) -> List[List[int]]:

        adjacency_list = [ [] for _ in range(cities_count) ]
        for [ source, sink, weight ] in edges:
            adjacency_list[source].append([ sink, weight ])

        return adjacency_list

    def __indegree(self, v: int, edges: List[List[int]]) -> int:
        indegree = 0
        for [ source, sink, weight ] in edges:
            if sink == v:
                indegree += 1
        
        return indegree

class Solution_BFS(Solution_Base):
    '''
        Time Complexity: O(|V|^2 + |V||E|) ?
            T = T(Build Adjacency List) + T(Kind Of BFS algo)
              = O(|E|)                  + |V| * O(|V| + |E|) 
            
        Space Complexity: O(|V| + |E|)
            S = S(Adjacency_list) + S(BFS Curr Level Queue) + S(BFS Next Level Queue) + S(Visited Hash Map)
              = O(|V| + |E|)      + O(|V|)                  + O(|V|)                  + O(|V|)
    
    '''
    def find_cheapest_price(self, cities_count: int, flights: List[List[int]], src: int, dst: int, max_stops_count: int) -> int:
        
        adjacency_list = self.__build_adjacency_list(cities_count, flights)

        if (self.__indegree(dst) == 0):
            return -1

        '''
            Each node (city) is potentially visited multiple times.
            Worst case: 
                - Successive pathes to a city have decreasing prices
                - Each city will be visited |V| times
            This would make the time complexity: T = |V| * T(Real BFS) = |V| * O(|V| + |E|) = O(|V|^2 + |V||E|) ?
        '''
        visited_cities = {}
        curr_level = [ (src, 0) ]
        cheapest_price = self.__max_pirce
        while curr_level:
            
            next_level = []
            for (city, price) in curr_level:
                if price >= cheapest_price:
                    continue
                
                for [ flight_to_city, flight_price ] in adjacency_list[city]:
                    
                    path_price = flight_price + price
                    if flight_to_city == dst:
                        cheapest_price = min(cheapest_price, path_price)
                        
                    elif path_price < cheapest_price and visited_cities.get(flight_to_city, self.__max_pirce) > path_price:
                        visited_cities[city] = path_price
                        next_level.append((flight_to_city, path_price))
            
            if max_stops_count == 0:
                break
            max_stops_count -= 1
            
            curr_level = next_level
        
        return -1 if cheapest_price == self.__max_pirce else cheapest_price

class Solution_DFS(Solution_Base):
    '''
        Time Complexity: O(K * |V|^2 + |E|)
            T = T(Build Adjacency List) + T(DFS algo)
              = O(|E|)                  + O(K * |V|^2)
            
        Space Complexity: O(K * |V| + |E|)
            S = S(Adjacency_list) + S(DFS)
              = O(|V| + |E|)      + O(K * |V|)
    
    '''
    def find_cheapest_price(self, cities_count: int, flights: List[List[int]], src: int, dst: int, max_stops_count: int) -> int:
        adjacency_list = self.__build_adjacency_list(cities_count, flights)

        if (self.__indegree(dst) == 0):
            return -1
        
        cheapest_price = self.__dfs(src, dst, adjacency_list, max_stops_count, {})
        return -1 if cheapest_price == self.__max_pirce else cheapest_price
    
    '''
            Assumption: remaining_stops_count = K < |V|
            Time complexity:
                depth         Nbr of problems          work at corresponding depth      space at corresponding depth
                0             1                        1 * O(outdegree(src)) = O(|V|)    O(1)
                1             |V|                      |V| * O(|V|) = O(|V|^2)           |V| * O(1)
                ...
                K             |V|                      O(|V|^2)                          O(|V|)

            Total time complexity:  O(K * |V|^2)
            Total space complexity: O(K * |V|)
        
        '''
    def __dfs(self, src: int, dst: int, adjacency_list: List[List[int]], remaining_stops_count: int, memo: dict) -> int:
        if src == dst:
            return 0 
        
        if remaining_stops_count == -1:
            return self.__max_pirce
        
        elif (src, remaining_stops_count) in memo:
            return memo[(src, remaining_stops_count)]
        
        cheapest_price = self.__max_pirce
        for [ flight_to, flight_pirce ] in adjacency_list[src]:
            cheapest_price = min(cheapest_price, self.__dfs(flight_to, dst, adjacency_list, remaining_stops_count - 1, memo) + flight_pirce)
        
        memo[(src, remaining_stops_count)] = cheapest_price
        return cheapest_price

class Solution_Dijktra(Solution_Base):
    '''
        Time Complexity: O(E * Log|E|)
            T = T(Build Adjacency List) + T(Dijkstra)
              = O(|E|)                  + O(E * Log|E|)
            
        Space Complexity: O(|V| + |E|)
            S = S(Adjacency_list) + S(Dijkstra)
              = O(|V| + |E|)      + O(|V| + |E|)
    
    '''
    def find_cheapest_price(self, cities_count: int, flights: List[List[int]], src: int, dst: int, max_stops_count: int) -> int:
        adjacency_list = self.__build_adjacency_list(cities_count, flights)

        if (self.__indegree(dst) == 0):
            return -1

        stops = [ max_stops_count+1 for _ in range(cities_count) ]
        prices = [ self.__max_pirce for _ in range(cities_count) ]
        stops[src], prices[src] = 0, 0

        cheapest_flights = [ (0, 0, src) ]
        while cheapest_flights:
            (path_price, path_stops, path_stop_city) = heapq.heappop(cheapest_flights) 
            if path_stop_city == dst:
                return path_price
            
            elif path_stop_city == max_stops_count + 1:
                continue

            for [ next_city, price ] in adjacency_list[path_stop_city]: # each edge can be pushed only 1 time into the heap
                candidate_path_price = path_price + price
                candidate_path_stops = path_stops + 1
                if candidate_path_price < prices[next_city]:
                    prices[next_city] = candidate_path_price
                    heapq.heappush(cheapest_flights, (candidate_path_price, candidate_path_stops, next_city))
                
                elif candidate_path_price < stops[next_city]:
                    heapq.heappush(cheapest_flights, (candidate_path_price, candidate_path_stops, next_city))
        
        return -1 if prices[dst] == self.__max_pirce else prices[dst]
