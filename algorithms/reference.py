from collections import deque

# ==========================================
# BREADTH FIRST SEARCH (BFS)
# ==========================================
# Used for: shortest path, level by level traversal
# Data structure: QUEUE
# Time: O(V+E) where V=vertices, E=edges

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()        # process front of queue
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbor in graph[node]:
                queue.append(neighbor)  # add neighbors to back of queue

# BFS on a tree (level by level)
def bfs_tree(root):
    if not root: return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)


# ==========================================
# DEPTH FIRST SEARCH (DFS)
# ==========================================
# Used for: exploring all paths, cycle detection, finding islands
# Data structure: STACK (or recursion)
# Time: O(V+E) where V=vertices, E=edges

# DFS recursive
def dfs_recursive(graph, node, visited=None):
    if visited is None: visited = set()
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# DFS iterative
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()            # process top of stack
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(reversed(graph[node]))  # add neighbors to stack


# ==========================================
# TREE TRAVERSALS
# ==========================================
# Used for: processing tree nodes in specific order
# Time: O(n) where n=number of nodes

# inorder: left -> root -> right (gives sorted order for BST)
def inorder(node):
    if not node: return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

# preorder: root -> left -> right (useful for copying a tree)
def preorder(node):
    if not node: return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

# postorder: left -> right -> root (useful for deleting a tree)
def postorder(node):
    if not node: return
    postorder(node.left)
    postorder(node.right)
    print(node.val)


# ==========================================
# SLIDING WINDOW
# ==========================================
# Used for: subarray/substring problems, finding max/min in a window
# Time: O(n) — avoids nested loops
# Two types: fixed size window and variable size window

# fixed size window (window of size k)
def fixed_window(arr, k):
    window_sum = sum(arr[:k])   # sum of first window
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]  # slide window: add new, remove old
        max_sum = max(max_sum, window_sum)
    return max_sum

# variable size window (expand/shrink based on condition)
def variable_window(arr, target):
    left = 0
    window_sum = 0
    min_len = float('inf')
    for right in range(len(arr)):
        window_sum += arr[right]           # expand window to the right
        while window_sum >= target:        # shrink window from the left
            min_len = min(min_len, right - left + 1)
            window_sum -= arr[left]
            left += 1
    return min_len


# ==========================================
# BINARY SEARCH
# ==========================================
# Used for: searching sorted arrays, finding boundaries
# Time: O(log n) — cuts search space in half each time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid    # found it
        elif arr[mid] < target: left = mid + 1   # go right
        else: right = mid - 1                # go left
    return -1  # not found

# binary search on a 2D matrix
def search_matrix(matrix, target):
    top, bottom = 0, len(matrix) - 1
    while top <= bottom:
        row_mid = (top + bottom) // 2
        if matrix[row_mid][0] <= target <= matrix[row_mid][-1]:
            left, right = 0, len(matrix[0]) - 1
            while left <= right:
                col_mid = (left + right) // 2
                if matrix[row_mid][col_mid] == target: return True
                elif matrix[row_mid][col_mid] < target: left = col_mid + 1
                else: right = col_mid - 1
            return False
        elif matrix[row_mid][0] > target: bottom = row_mid - 1
        else: top = row_mid + 1
    return False


# ==========================================
# TOPOLOGICAL SORT
# ==========================================
# Used for: ordering tasks with dependencies, course scheduling
# Only works on Directed Acyclic Graphs (DAG)
# Time: O(V+E)

def topological_sort(graph):
    visited = set()
    result = []

    def dfs(node):
        if node in visited: return
        visited.add(node)
        for neighbor in graph[node]:  # visit all dependencies first
            dfs(neighbor)
        result.append(node)           # add node AFTER all dependencies

    for node in graph:
        dfs(node)

    return result[::-1]  # reverse to get correct order

# example: course prerequisites
# graph = {0: [1], 1: [2], 2: []} means course 0 requires 1, 1 requires 2
# topological order: [0, 1, 2]