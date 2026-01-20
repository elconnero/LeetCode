# Trees

## Overview
Hierarchical data structure with nodes connected by edges. Each node has a parent (except root) and zero or more children.

## Types
- **Binary Tree** - Each node has at most 2 children
- **Binary Search Tree (BST)** - Left < Parent < Right
- **Balanced Trees** - AVL, Red-Black (height-balanced)
- **N-ary Tree** - Nodes can have N children

## Common Patterns
- **DFS Traversals** - Inorder, Preorder, Postorder
- **BFS (Level Order)** - Using queue for level-by-level
- **Recursion** - Most tree problems solved recursively

## Key Operations (BST)
| Operation | Average | Worst |
|-----------|---------|-------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

## Common Problems
- Maximum Depth of Binary Tree
- Validate BST
- Invert Binary Tree
- Lowest Common Ancestor
- Binary Tree Level Order Traversal
