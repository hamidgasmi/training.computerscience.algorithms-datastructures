# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class SolutionDFS:
    
    def __init__(self):
        
        self.directions = [1,2,-1,-2]
        
        self.up     = 1
        self.right  = 2
        self.down   = -1
        self.left   = -2
    
    def clean_room(self, robot):
        
        self.cleaned = set()
        self.robot = robot
        
        self.clean_room_dfs(0, 0, 0)
        
    def clean_room_dfs(self, row, col, direct_idx):
        
        self.robot.clean()
        self.cleaned.add((row, col))
        
        cleaned_directions = set()
        
        curr_direct_idx = direct_idx
        while len(cleaned_directions) < 4:
            if curr_direct_idx not in cleaned_directions:
                cleaned_directions.add(curr_direct_idx)
                
                next_row, next_col = self.next_position(row, col, self.directions[curr_direct_idx])
                
                if (next_row, next_col) not in self.cleaned and self.robot.move():
                    curr_direct_idx = self.clean_room_dfs(next_row, next_col, curr_direct_idx)
            
            else:
                curr_direct_idx = (curr_direct_idx + 1) % 4
                self.robot.turnRight()
        
        opposite_direct_idx = self.directions.index(self.directions[direct_idx] * (-1))
        if curr_direct_idx != opposite_direct_idx:
            if self.directions[(curr_direct_idx + 1) % 4] == self.directions[opposite_direct_idx]:
                self.robot.turnRight()
                
            elif self.directions[(curr_direct_idx - 1 + 4) % 4] == self.directions[opposite_direct_idx]:
                self.robot.turnLeft()
                
            else:
                self.robot.turnRight()
                self.robot.turnRight()
        
        self.robot.move()
        return opposite_direct_idx
    
    def next_position(self, row, col, direction):
        assert(direction in (self.up, self.down, self.right, self.left))
        
        if direction == self.up:
            return row - 1, col
        
        elif direction == self.down:
            return row + 1, col
        
        elif direction == self.right:
            return row, col + 1
        
        else:
            return row, col - 1
