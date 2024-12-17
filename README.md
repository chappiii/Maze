# Maze Solver: A*, BFS, and DFS Algorithms

This project implements **A***, **Breadth-First Search (BFS)**, and **Depth-First Search (DFS)** algorithms to solve a maze provided in a JSON file. The solution compares performance metrics like path length, runtime, memory usage, and optimality.

---

## Table of Contents

- [Usage Instructions](#usage-instructions)
- [Algorithm Implementations](#algorithm-implementations)
- [Performance Metrics](#performance-metrics)
- [Strengths and Weaknesses](#strengths-and-weaknesses)
- [Most Suitable Algorithm](#most-suitable-algorithm)
- [Conclusion](#conclusion)
- [Sample Maze Input](#sample-maze-input)
- [Future Improvements](#future-improvements)

---

## Usage Instructions

Run the program with the following commands:

- **A*** Algorithm:
   ```bash
   python A.py maze.json
   ```

- **Breadth-First Search (BFS):**
   ```bash
   python BFS.py maze.json
   ```

- **Depth-First Search (DFS):**
   ```bash
   python DFS.py maze.json
   ```

Make sure to replace `maze.json` with your maze file.

---

## Algorithm Implementations

### 1. **A\*** Algorithm
- **Initialization**: Uses a **priority queue** (`heapq`) and the **Manhattan distance** heuristic.
- **Mechanism**: Prioritizes nodes based on their f-score:
   \[
   \text{f-score} = \text{g-score} + \text{heuristic}
   \]
- **Behavior**: Explores nodes with the lowest f-score, updates costs (`g_score`), and tracks the path (`came_from`).
- **Goal**: Stops when the goal is reached or all nodes are exhausted.

### 2. **Breadth-First Search (BFS)**
- **Initialization**: Uses a **queue-based frontier** to explore nodes level-by-level.
- **Mechanism**: Adds unvisited neighbors to the queue while tracking explored states.
- **Goal**: Stops when the goal is reached or all nodes are exhausted.

### 3. **Depth-First Search (DFS)**
- **Initialization**: Uses a **stack-based frontier** to explore nodes deeper first.
- **Mechanism**: Tracks explored states and reconstructs the path by backtracking.
- **Goal**: Stops when the goal is reached or all nodes are exhausted.

---

## Performance Metrics

| **Metric**         | **A\***          | **BFS**          | **DFS**          |
|---------------------|------------------|------------------|------------------|
| **Path Optimality** | Optimal          | Optimal          | Not Guaranteed   |
| **Path Length**     | 26 steps         | 26 steps         | 26 steps         |
| **Memory Usage**    | Least Memory     | Most Memory      | Moderate Memory  |
| **Runtime**         | Fastest          | Slowest          | Faster than BFS  |

---

## Strengths and Weaknesses

### **A\***
- **Strengths**:
   - Finds the optimal path.
   - Efficient due to heuristic guidance.
   - Flexible for different heuristics.
- **Weaknesses**:
   - Memory-intensive.
   - Performance depends on the heuristic.

### **Breadth-First Search (BFS)**
- **Strengths**:
   - Guaranteed optimal path.
   - Simple and easy to implement.
- **Weaknesses**:
   - High memory usage.
   - Slow for large mazes.

### **Depth-First Search (DFS)**
- **Strengths**:
   - Memory efficient.
   - Fast for simple or small mazes.
- **Weaknesses**:
   - Non-optimal paths.
   - Can get stuck in loops or dead-ends.

---

## Most Suitable Algorithm

The **A\*** Search Algorithm is the most suitable for solving the maze problem due to its:

- **Optimality**: Finds the shortest path.
- **Efficiency**: Uses heuristic guidance to minimize exploration.
- **Memory Usage**: Better than BFS.

### Alternatives:
- **BFS**: Suitable when path optimality is critical and memory usage is not a concern.
- **DFS**: Works for small or simple mazes where finding *any path quickly* is more important than the optimal path.

---

## Conclusion

All three algorithms successfully solved the provided maze with the same path length (26 steps). However:

- **A\*** was the fastest and most memory-efficient.
- **BFS** guaranteed optimality but consumed the most memory.
- **DFS** was faster than BFS but is not guaranteed to find the optimal path.

For most maze-solving problems, **A\*** is the preferred choice.

---

## Future Improvements
- Support for other heuristics in A\*.
- Visualization of paths explored.
- Benchmarking on larger mazes.

---

---