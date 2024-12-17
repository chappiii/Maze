import sys
import json
import heapq
import time   
import tracemalloc  
import os 

class AStarMaze:
    def __init__(self, maze, start, goal):
        self.maze = maze
        self.start = start
        self.goal = goal
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.open_list = []  
        self.closed_list = set()  
        self.g_score = {}  
        self.f_score = {}  
        self.came_from = {}
        self.solution = None
        self.states_explored = 0 

    # heuristic Manhattan distance 
    def heuristic(self, node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    # Get neighbors of the current node that are within the maze and walkable
    def neighbors(self, node):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        for d in directions:
            neighbor = (node[0] + d[0], node[1] + d[1])
            if 0 <= neighbor[0] < self.rows and 0 <= neighbor[1] < self.cols:
                if self.maze[neighbor[0]][neighbor[1]] == 0:
                    neighbors.append(neighbor)
        return neighbors

    # Main method to run the A* algorithm
    def run(self):
        # Initialize the start node with g_score 0 and f_score heuristic value
        self.g_score[self.start] = 0
        self.f_score[self.start] = self.heuristic(self.start, self.goal)
        heapq.heappush(self.open_list, (self.f_score[self.start], self.start))

        # While there are nodes to explore
        while self.open_list:
            current_f, current_node = heapq.heappop(self.open_list)
            
            # If the goal is reached, reconstruct the path
            if current_node == self.goal:
                self.solution = self.find_path(self.goal)
                return self.solution

            self.closed_list.add(current_node)
            self.states_explored += 1  
            
            neighbors = self.neighbors(current_node)
            for neighbor in neighbors:
                if neighbor in self.closed_list:
                    continue
                
                tentative_g_score = self.g_score.get(current_node, float('inf')) + 1
                # If the neighbor node has a better path, update its scores and path
                if neighbor not in self.g_score or tentative_g_score < self.g_score[neighbor]:
                    self.came_from[neighbor] = current_node
                    self.g_score[neighbor] = tentative_g_score
                    self.f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.goal)
                    
                    if neighbor not in [n for f, n in self.open_list]:
                        heapq.heappush(self.open_list, (self.f_score[neighbor], neighbor))

        return None  

    # Reconstruct the path from start to goal
    def find_path(self, goal):
        path = []
        current = goal
        while current in self.came_from:
            path.append(current)
            current = self.came_from[current]
        path.append(current)
        path.reverse()
        return path

    # Print the maze with the solution path, if found
    def print(self):
        solution = self.solution if self.solution is not None else None
        for i, row in enumerate(self.maze):
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

# Load maze data from the specified file
def load_maze(filename):
    if not os.path.exists(filename):
        sys.exit(f"Error: File '{filename}' not found. Please provide a valid maze file.\nUsage: python maze.py maze.json")
    
    with open(filename) as f:
        contents = json.load(f)
        
    contents_maze = contents["maze"]
    contents_start = contents["start"]
    contents_goal = contents["goal"]

    # Validate start and goal positions
    if contents_start[0] < 0 or contents_start[0] >= len(contents_maze) or contents_start[1] < 0 or contents_start[1] >= len(contents_maze[0]):
        raise Exception("Invalid start position, out of maze bounds")
    if contents_goal[0] < 0 or contents_goal[0] >= len(contents_maze) or contents_goal[1] < 0 or contents_goal[1] >= len(contents_maze[0]):
        raise Exception("Invalid goal position, out of maze bounds")

    return contents_maze, tuple(contents_start), tuple(contents_goal)

# Ensure the correct number of arguments is provided
if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.json")

filename = sys.argv[1]

# Load the maze, start, and goal from the JSON file
maze_data, start_position, goal_position = load_maze(filename)

# Run A* algorithm on the maze
astar_maze = AStarMaze(maze_data, start_position, goal_position)

# Print the maze before solving
print("Maze:")
print()
astar_maze.print()

# Measure the start time
starttime = time.perf_counter()

# Start tracking memory usage
tracemalloc.start()

# Solve the maze
print("Solving...")
solution_path = astar_maze.run()

# Measure runtime and memory usage
endtime = time.perf_counter()
runtime = endtime - starttime
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Print the solution and performance metrics if the solution is found
if solution_path:
    print("Solution found.")
    print(f"States Explored: {astar_maze.states_explored}")
    print(f"Runtime: {runtime:.8f} seconds")
    print(f"Memory Usage: Current = {current / 10**6:.4f} MB; Peak = {peak / 10**6:.4f} MB")
    print("Solution:")
    print()
    astar_maze.print()
else:
    print("No solution exists for the maze.")
    print(f"Runtime: {runtime:.8f} seconds")
    print(f"Memory Usage: Current = {current / 10**6:.4f} MB; Peak = {peak / 10**6:.4f} MB")
