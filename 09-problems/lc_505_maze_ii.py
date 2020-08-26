"""
    1. Problem Summary / Clarifications / TDD:
    2. Inuition:
        - Shortest path + all distances are positive 
        - Dijkstra's Algorithm
    3. Implementation:
    4. Complexity Analysis:
        - Time Complexity: O(O((R + C) * R*C))?
            - T(Initialization): O(R*C)
            - T(heap.pop): O(R*C*logR*C)
            - T(get_adjacency_list) = O((R + C) * R*C)
            - T(heap.push): O(4*R*C*logR*C)
            - Total: O(R*C) + O(R*C*logR*C) + O((R + C) * R*C) + O(4*R*C*logR*C)

"""

import heapq

class Solution:

    def __init__(self):
        self.__empty = 0
        self.__wall = 0
    
    # Time Complexity: O(R*C) + O(R*C*log(R*C)) + O((R+C)R*Clog(R*C)) = O((R+C)R*Clog(R*C))
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        rows_count = len(maze)
        cols_count = len(maze[0])
        
        distances = [[10001 for _ in range(cols_count)] for _ in range(rows_count)]
        distances[start[0]][start[1]] = 0
        
        priority_q = [[0, start[0], start[1]]]
        
        while priority_q: # O(R*C)
            
            position = heapq.heappop(priority_q) # O(log(R*C))
            
            for adjacent in self.__get_adjacency_list(maze, position): # O(R + C)
                
                if adjacent[0] < distances[adjacent[1]][adjacent[2]]:
                    distances[adjacent[1]][adjacent[2]] = adjacent[0]
                    heapq.heappush(priority_q, adjacent) # O(log(R*C))           
        
        return -1 if distances[ destination[0] ][ destination[1] ] == 10001 else distances[ destination[0] ][ destination[1] ]
    
    # Time Complexity: O(rows + colums) = O(R + C)
    # Space Complexity: O(4) = O(1)
    def __get_adjacency_list(self, maze, position: List[int]) ->List[List[int]]:
        
        adjacents = []
        
        rows_count = len(maze)
        cols_count = len(maze[0])
        
        dist, row, col = position[0], position[1], position[2]
        
        # Up
        steps_count = 0
        while row - steps_count and maze[row - steps_count - 1][col] == self.__empty:
            steps_count += 1
        if steps_count:
            adjacents.append([dist + steps_count, row - steps_count, col])
            
        # Down
        steps_count = 0
        while row + steps_count + 1 < rows_count and maze[row + steps_count + 1][col] == self.__empty:
            steps_count += 1
        if steps_count:
            adjacents.append([dist + steps_count, row + steps_count, col])
            
        # left
        steps_count = 0
        while col - steps_count and maze[row][col - steps_count - 1] == self.__empty:
            steps_count += 1
        if steps_count:
            adjacents.append([dist + steps_count, row, col - steps_count])
            
        # Right
        steps_count = 0
        while col + steps_count + 1 < cols_count and maze[row][col + steps_count + 1] == self.__empty:
            steps_count += 1
        if steps_count:
            adjacents.append([dist + steps_count, row, col + steps_count])
            
        return adjacents