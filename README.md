N.B. Run the programs using the commands “python A.py maze.json” for A*, “python BFS.py maze.json” for BFS, or “python DFS.py maze.json” for DFS to solve the maze in the provided JSON file. 
Implementation Details
A* Implementation- initializes the maze, start, and goal positions, using a priority queue (heapq) and the Manhattan distance heuristic to prioritize nodes in the open list based on their f-score (g-score + heuristic). It explores nodes with the lowest f-score, updating costs (g_score) and paths (came_from) as it explores neighbors, stopping when the goal is reached, or all nodes are exhausted.
BFS Implementation- initializes the maze, start, and goal positions, using a queue-based frontier (QueueFrontier) to explore nodes level-by-level. It tracks explored states, adding unvisited neighbors to the frontier, and stops when the goal is reached, or all nodes are exhausted.
DFS Implementation- initializes a maze, start, and goal using a stack-based frontier (StackFrontier) to explore nodes using depth-first search. It tracks explored states and explores deeper nodes first by adding unvisited neighbors to the frontier. The solution path is reconstructed by backtracking from the goal.
Performance Metrics
Path Optimality: Both A* and BFS found the optimal path. DFS found the same path in this case but is not guaranteed.
Path Length: All three found the same path length (26 steps).
Memory Usage: A* used the least memory effectively. BFS used the most memory due to extensive state storage. DFS used more memory than A* but less than BFS.
Runtime: A* was the fastest, followed by DFS, then BFS.
Strengths and Weaknesses
A* Strengths: Optimal, Efficient, Flexibility. A* Weaknesses: Memory Intensive, Heuristic Dependent
BFS Strengths: Guaranteed Optimality, Simple Implementation. BFS Weaknesses: High Memory Usage, Slow
DFS Strengths: Memory Efficient, Fast in Some Cases. DSF Weaknesses: Non-optimal, Can Get Stuck 
Most Suitable Algorithm for the Maze Problem
A* Search Algorithm is the most suitable due to its optimality and efficiency in finding the shortest path. BFS is a good alternative if the path length in terms of steps is the primary concern. DFS can be considered for smaller or simpler mazes where finding any path quickly is more critical than finding the optimal path. In the provided test case, all three algorithms found the goal, but A* was the fastest and used the least memory due to its heuristic guidance, making it the most efficient and suitable choice for the maze problem.
