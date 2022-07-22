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
        - Naive:
        - We could do better:

    3. Implementation
    4. Tests:
    5. Complexity Analysis:
       Time Complexity:
       Space Compexity:

"""

class Solution:
    
    import heapq

class Solution_Base:
    def __init__(self):
        self.__max_pirce = 10**8

    """
        Time Complexity: O(|E|)
        Space Complexity: O(|V| + |E|)
    """
    def __build_adjacency_list(self, cities_count: int, flights: List[List[int]]) -> List[List[int]]:
        adjacency_list = [ [] for _ in range(cities_count) ]
        for [ flight_from, flight_to, flight_pirce ] in flights:
            adjacency_list[flight_from].append([ flight_to, flight_pirce ])

        return adjacency_list
    