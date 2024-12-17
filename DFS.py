import sys
import json
import time  
import tracemalloc  
import os

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

# Stack to keeps track of nodes that need to be explored next
class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class Maze():

    # Check if the specified maze file exists.
    def __init__(self, filename):
        if not os.path.exists(filename):
            sys.exit(f"Error: File '{filename}' not found. Please provide a valid maze file.\nUsage: python maze.py maze.json")

        # Load maze configuration from the JSON file.
        with open(filename) as f:
            contents = json.load(f)
            
        contents_maze = contents["maze"]
        contents_start = contents["start"]
        contents_goal = contents["goal"]

        # Check if the start position is within the maze
        if contents_start[0] < 0 or contents_start[0] >= len(contents_maze) or contents_start[1] < 0 or contents_start[1] >= len(contents_maze[0]):
            raise Exception("Invalid start position, out of maze bounds")
        # Check if the goal position is within the maze 
        if contents_goal[0] < 0 or contents_goal[0] >= len(contents_maze) or contents_goal[1] < 0 or contents_goal[1] >= len(contents_maze[0]):
            raise Exception("Invalid goal position, out of maze bounds")
        
        self.height = len(contents_maze)
        self.width = max(len(line) for line in contents_maze)

        # Construct walls based on the maze configuration,
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if (i, j) == tuple(contents_start):
                    self.start = (i, j)
                    row.append(False)  
                elif (i, j) == tuple(contents_goal):
                    self.goal = (i, j)
                    row.append(False)  
                elif contents_maze[i][j] == 0:  
                    row.append(False)
                else:
                    row.append(True)  
            self.walls.append(row)

        self.solution = None

    # Print the maze with the solution path if available.
    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print(" 1 ", end="")
                elif (i, j) == self.start:
                    print(" S ", end="")
                elif (i, j) == self.goal:
                    print(" G ", end="")
                elif solution is not None and (i, j) in solution:
                    print(" * ", end="")
                else:
                    print(" 0 ", end="")
            print()
        print()

    # Return all possible moves from the current state
    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result
    
    # Main method to run the algorithm
    def solve(self):

        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        self.explored = set()

        # Keep looping until solution found
        while True:

            if frontier.empty():
                self.solution = None
                return "No solution exists for the maze."

            node = frontier.remove()
            self.num_explored += 1

            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return "Solution found."

            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

# Ensure the correct number of arguments are provided.
if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.json")

# Start performance and memory tracking.
starttime = time.perf_counter() 
tracemalloc.start()

# Load the maze and print the initial state.
m = Maze(sys.argv[1])
print("Maze:")
m.print()

print("Solving...")
result = m.solve()  

# Stop performance tracking.
endtime = time.perf_counter() 
runtime = endtime - starttime

# Get memory usage.
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Print the result and performance metrics.
print(result)
if result == "Solution found.":
    print("States Explored:", m.num_explored)
    print(f"Runtime: {runtime:.8f} seconds")
    print(f"Memory Usage: Current = {current / 10**6:.4f} MB; Peak = {peak / 10**6:.4f} MB")
    print("Solution:")
    m.print()
else:
    print(f"Runtime: {runtime:.8f} seconds")
    print(f"Memory Usage: Current = {current / 10**6:.4f} MB; Peak = {peak / 10**6:.4f} MB")
