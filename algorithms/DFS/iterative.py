from algorithms.DFS.globals import tree

def dfs_iterative(tree, start):

    visited = set() # This is what we will use to track visited nodes
    stack = [start] # This is the stack for the DFS

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(reversed(tree[node])) # Adding child nodes to the stack

dfs_iterative(tree, 'A')