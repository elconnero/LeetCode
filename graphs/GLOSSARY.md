# Graphs

## Overview
Collection of nodes (vertices) connected by edges. Can be directed or undirected, weighted or unweighted.

## Representations
- **Adjacency List** - Map of node to list of neighbors (most common)
- **Adjacency Matrix** - 2D array of edge connections
- **Edge List** - List of (source, destination, weight) tuples

## Common Patterns
- **BFS** - Shortest path in unweighted graphs, level-order
- **DFS** - Connectivity, cycle detection, topological sort
- **Union-Find** - Connected components, cycle detection
- **Dijkstra/Bellman-Ford** - Shortest path in weighted graphs

## Key Operations
| Algorithm | Time Complexity |
|-----------|-----------------|
| BFS/DFS | O(V + E) |
| Dijkstra | O((V + E) log V) |
| Union-Find | O(α(n)) per operation |

## Common Problems
- Number of Islands
- Clone Graph
- Course Schedule (Topological Sort)
- Word Ladder
- Network Delay Time
